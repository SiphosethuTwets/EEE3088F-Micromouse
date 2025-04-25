import pcbnew
import kicad
from kicad import Point

def create_usb_power_delivery_sheet():
    # Get the current project and schematic
    proj = pcbnew.GetCurrentProject()
    schematic = proj.GetCurrentSchematic()
    
    # 1. Create new sheet
    sheet = schematic.AddSheet("USB_Power_Delivery")
    schematic.SetActiveSheet(sheet)
    
    # 2. Place components
    # A. USB-C Connector
    usb_c = schematic.AddSymbol(Point(100000000, 100000000), "Connector_USB:USB_C_Receptacle_USB2.0")
    usb_c.SetReference("USB1")
    
    # B. STUSB4500
    stusb = schematic.AddSymbol(Point(150000000, 100000000), "ST_USB:STUSB4500")
    stusb.SetReference("U1")
    
    # C. 10kΩ Resistor
    resistor = schematic.AddSymbol(Point(120000000, 80000000), "Device:R")
    resistor.SetReference("R1")
    resistor.SetValue("10k")
    
    # 3. Wiring & Net Labels
    # A. Power Path
    # USB1.VBUS to STUSB4500.VBUS_EN_SNK
    schematic.AddWire([
        usb_c.GetPin("VBUS").GetPosition(),
        Point(130000000, 100000000),
        stusb.GetPin("VBUS_EN_SNK").GetPosition()
    ])
    
    # Add net labels
    schematic.AddNetLabel("USB_VBUS", Point(125000000, 105000000))
    schematic.AddNetLabel("9V_OUT", Point(160000000, 105000000))
    
    # B. CC Lines
    schematic.AddWire([
        usb_c.GetPin("CC1").GetPosition(),
        resistor.GetPin("1").GetPosition()
    ])
    schematic.AddWire([
        resistor.GetPin("2").GetPosition(),
        Point(120000000, 70000000),  # GND point
    ])
    schematic.AddWire([
        usb_c.GetPin("CC1").GetPosition(),
        stusb.GetPin("CC1").GetPosition()
    ])
    
    # 4. Assign footprints (JLCPCB)
    usb_c.SetFootprint("Connector_USB:USB_C_Receptacle_USB2.0")
    stusb.SetFootprint("Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm")
    resistor.SetFootprint("Resistor_SMD:R_0805_2012Metric")
    
    # 5. Add power flags
    pwr_flag = schematic.AddSymbol(Point(125000000, 110000000), "power:PWR_FLAG")
    pwr_flag.GetPin("1").Connect(schematic.FindNet("USB_VBUS"))
    
    pwr_flag2 = schematic.AddSymbol(Point(160000000, 110000000), "power:PWR_FLAG")
    pwr_flag2.GetPin("1").Connect(schematic.FindNet("9V_OUT"))
    
    # Refresh the view
    schematic.UpdateAll()
    print("USB Power Delivery sheet created successfully!")

# Run the function
create_usb_power_delivery_sheet()