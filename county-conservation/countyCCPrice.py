from nicegui import ui

triDeliveryDict = {'Absecon': 370, 'Alloway': 240, 'Atco': 270, 'Atlantic City': 420, 'Audubon': 200, 'Audubon Park': 200, 'Avalon': 350,
                'Barrington': 200, 'Bass River Township': 395, 'Bellmawr': 200, 'Berlin': 200, 'Berlin Township': 200,
                'Beverly': 320, 'Blackwood': 160, 'Blue Anchor': 220, 'Bordentown': 395, 'Bordentown Township': 340, 'Bridgeton': 320,
                'Brigatine': 420, 'Brooklawn': 180, 'Buena': 210, 'Buena Vista': 370, 'Burlington': 320, 'Burlington Township': 320,
                'Camden': 420, 'Cape May': 395, 'Cape May Courthouse': 395, 'Cape May Point': 420, 'Carneys Point': 270, 'Cherry Hill': 270,
                'Chesilhurst': 215, 'Chesterfield Township': 340, 'Cinnaminson Township': 280, 'Clayton': 160, 'Clarksboro': 200, 'Clementon': 180,
                'Collingswood': 200, 'Commercial Township': 310, 'Corbin City': 380, 'Deerfield Township': 160, 'Delanco': 270, 'Delran': 295,
                'Dennis': 340, 'Deptford': 180, 'Downe Township': 310, 'East Greenwich Township': 180, 'Eastampton': 320, 'Edgewater Park': 320,
                'Egg Harbor City': 380, 'Egg Harbor Township': 380, 'Elk Township': 160, 'Elmer': 190, 'Elsinboro': 300, 'Estell Manor': 380,
                'Evesham': 300, 'Fairfield Township': 320, 'Fieldsboro': 330, 'Florence Township': 320, 'Folsom': 370, 'Franklin Township': 160,
                'Galloway': 370, 'Gibbsboro': 200, 'Gibbstown': 180, 'Glassboro': 160, 'Glendora': 190, 'Gloucester City': 190, 'Gloucester Township': 160,
                'Greenwich Township': 320, 'Haddon Heights': 320, 'Haddon Township': 180, 'Haddonfield': 210, 'Hainesport': 210,
                'Hamilton Township': 370, 'Hammonton': 370, 'Harrison Township': 210, 'Hi-Nella': 180, 'Hopewell Township': 320,
                'Laurel Springs': 180, 'Lawnside': 190, 'Lawrence Township': 320, 'Lindenwold': 200, 'Linwood': 370, 'Logan Township': 210,
                'Longwood': 420, 'Lower': 400, 'Lower Alloways Creek': 380, 'Lumberton': 320, 'Magnolia': 180, 'Mannington': 220, 'Mays Landing': 370,
                'Mansfield': 330, 'Mantua Township': 160, 'Maple Shade': 220, 'Margate': 420, 'Marlton': 340, 'Maurice River': 320,
                'Medford': 320, 'Medford Lakes': 320, 'Medford Township': 320, 'Merchantville': 220, 'Mickleton': 200, 'Middle': 340,
                'Millville': 160, 'Monroeville': 180, 'Monroe Township': 180, 'Moorestown': 320, 'Mount Ephraim': 180, 'Mount Holly': 270, 'Mount Laurel': 300,
                'Mount Royal': 200, 'Mullica Hill': 200, 'Mullica Township': 370, 'National Park': 180, 'New Hanover': 320, 'Newfield': 180,
                'North Hanover': 420, 'North Wildwood': 395, 'Northfield': 380, 'Oaklyn': 180, 'Ocean City': 420, 'Oldmans': 210, 'Palmyra': 270,
                'Paulsboro': 180, 'Pedricktown': 210, 'Pemberton': 320, 'Penns Grove': 270, 'Pennsauken Township': 220, 'Pennsville': 295,
                'Pilesgrove': 210, 'Pine Hill': 190, 'Pine Valley': 190, 'Pitman': 180, 'Pittsgrove': 240, 'Pleasantville': 380, 'Port Norris': 320, 'Port Republic': 385,
                'Quinton': 240, 'Riverside': 295, 'Riverton': 295, 'Runnemede': 190, 'Salem': 250, 'Sea Isle': 340, 'Sewell': 160, 'Shamong': 300,
                'Shiloh': 320, 'Sicklerville': 200, 'Somerdale': 180, 'Somers Point': 390, 'South Harrison': 180, 'Southampton': 300, 'Springfield': 330,
                'Stone Harbor': 350, 'Stow Creek Township': 320, 'Stratford': 180, 'Swedesboro': 180, 'Tabernacle': 300, 'Tavistock': 210,
                'Tuckerton': 380, 'Turnersville': 160, 'Upper': 330, 'Upper Deerfield Township': 310, 'Upper Pittsgrove': 220, 'Ventnor City': 420,
                'Vincetown': 150, 'Vineland': 80, 'Voorhees Township': 100, 'Washington Township': 80, 'Waterford Township': 110, 'Wenonah': 95,
                'West Cape May': 420, 'West Deptford': 210, 'West Wildwood': 380, 'Westampton Township': 310, 'Westville': 210,
                'Weymouth Township': 380, 'Wildwood': 138090, 'Wildwood Crest': 380, 'Williamstown': 200, 'Willingboro': 320, 'Winslow Township': 220,
                'Woodbine': 340, 'Woodbury': 180, 'Woodbury Heights': 170, 'Woodland Township': 370, 'Woodlynne': 210, 'Woodstown': 210, 'Woolwich Township': 180}

deliveryDict = {'Absecon': 195, 'Alloway': 130, 'Atco': 145, 'Atlantic City': 220, 'Audubon': 110, 'Audubon Park': 110, 'Avalon': 185,
                'Barrington': 110, 'Bass River Township': 210, 'Bellmawr': 120, 'Berlin': 120, 'Berlin Township': 120,
                'Beverly': 170, 'Blackwood': 80, 'Blue Anchor': 120, 'Bordentown': 210, 'Bordentown Township': 180, 'Bridgeton': 170,
                'Brigatine': 220, 'Brooklawn': 120, 'Buena': 105, 'Buena Vista': 195, 'Burlington': 180, 'Burlington Township': 180,
                'Camden': 220, 'Cape May': 220, 'Cape May Courthouse': 220, 'Cape May Point': 220, 'Carneys Point': 150, 'Cherry Hill': 135,
                'Chesilhurst': 120, 'Chesterfield Township': 180, 'Cinnaminson Township': 150, 'Clayton': 80, 'Clarksboro': 95, 'Clementon': 90,
                'Collingswood': 105, 'Commercial Township': 165, 'Corbin City': 200, 'Deerfield Township': 80, 'Delanco': 180, 'Delran': 160,
                'Dennis': 180, 'Deptford': 90, 'Downe Township': 165, 'East Greenwich Township': 90, 'Eastampton': 170, 'Edgewater Park': 170,
                'Egg Harbor City': 200, 'Egg Harbor Township': 200, 'Elk Township': 90, 'Elmer': 105, 'Elsinboro': 160, 'Estell Manor': 180,
                'Evesham': 160, 'Fairfield Township': 170, 'Fieldsboro': 175, 'Florence Township': 170, 'Folsom': 195, 'Franklin Township': 80,
                'Galloway': 195, 'Gibbsboro': 110, 'Gibbstown': 90, 'Glassboro': 90, 'Glendora': 95, 'Gloucester City': 95, 'Gloucester Township': 90,
                'Greenwich Township': 170, 'Haddon Heights': 100, 'Haddon Township': 110, 'Haddonfield': 110, 'Hainesport': 170,
                'Hamilton Township': 195, 'Hammonton': 195, 'Harrison Township': 110, 'Hi-Nella': 90, 'Hopewell Township': 170,
                'Laurel Springs': 100, 'Lawnside': 105, 'Lawrence Township': 170, 'Lindenwold': 100, 'Linwood': 195, 'Logan Township': 105,
                'Longwood': 220, 'Lower': 210, 'Lower Alloways Creek': 200, 'Lumberton': 170, 'Magnolia': 95, 'Mannington': 120, 'Mays Landing': 195,
                'Mansfield': 220, 'Mantua Township': 85, 'Maple Shade': 120, 'Margate': 200, 'Marlton': 160, 'Maurice River': 170,
                'Medford': 170, 'Medford Lakes': 170, 'Medford Township': 170, 'Merchantville': 120, 'Mickleton': 110, 'Middle': 160,
                'Millville': 90, 'Monroeville': 95, 'Monroe Township': 95, 'Moorestown': 160, 'Mount Ephraim': 90, 'Mount Holly': 135, 'Mount Laurel': 150,
                'Mount Royal': 100, 'Mullica Hill': 100, 'Mullica Township': 185, 'National Park': 90, 'New Hanover': 160, 'Newfield': 90,
                'North Hanover': 210, 'North Wildwood': 200, 'Northfield': 190, 'Oaklyn': 90, 'Ocean City': 210, 'Oldmans': 105, 'Palmyra': 135,
                'Paulsboro': 90, 'Pedricktown': 105, 'Pemberton': 160, 'Penns Grove': 135, 'Pennsauken Township': 110, 'Pennsville': 150,
                'Pilesgrove': 105, 'Pine Hill': 95, 'Pine Valley': 95, 'Pitman': 90, 'Pittsgrove': 120, 'Pleasantville': 190, 'Port Norris': 160, 'Port Republic': 200,
                'Quinton': 120, 'Riverside': 150, 'Riverton': 150, 'Runnemede': 95, 'Salem': 125, 'Sea Isle': 170, 'Sewell': 80, 'Shamong': 150,
                'Shiloh': 160, 'Sicklerville': 100, 'Somerdale': 90, 'Somers Point': 195, 'South Harrison': 90, 'Southampton': 150, 'Springfield': 165,
                'Stone Harbor': 175, 'Stow Creek Township': 160, 'Stratford': 90, 'Swedesboro': 90, 'Tabernacle': 150, 'Tavistock': 105,
                'Tuckerton': 190, 'Turnersville': 80, 'Upper': 165, 'Upper Deerfield Township': 155, 'Upper Pittsgrove': 110, 'Ventnor City': 210,
                'Vincetown': 150, 'Vineland': 80, 'Voorhees Township': 100, 'Washington Township': 80, 'Waterford Township': 110, 'Wenonah': 95,
                'West Cape May': 210, 'West Deptford': 105, 'West Wildwood': 190, 'Westampton Township': 155, 'Westville': 105,
                'Weymouth Township': 190, 'Wildwood': 190, 'Wildwood Crest': 190, 'Williamstown': 100, 'Willingboro': 160, 'Winslow Township': 110,
                'Woodbine': 170, 'Woodbury': 90, 'Woodbury Heights': 85, 'Woodland Township': 185, 'Woodlynne': 105, 'Woodstown': 105, 'Woolwich Township': 90}

matDict = {'Aged Bark Mulch': 52, 'Cedar Mulch': 52.5, 'Black Dyed Mulch': 27, 'Brown Dyed Mulch': 27, 'Red Dyed Mulch': 36,
           'Premium Root Mulch': 22, 'Premium Hardwood': 19, 'Playground Mulch': 24, 'Virgin Woodchips': 12, 'Top Soil': 26,
           'Compost': 19, 'Fill Dirt': 15, 'DGA': 26, '3/4" River Rock': 70, '1.5" x 3" River Rock': 95, '3" x 5" River Rock': 95,
           '3/4" Red Driveway Stone': 50, '3/4" Grey Driveway Stone': 50, 'Modified Stone 2A': 38, 'Stone Dust Screenings': 38,
           'Pea Gravel': 54, 'Sand': 28}

matShortcuts = {'bark mulch': 'Aged Bark Mulch', 'Bark Mulch': 'Aged Bark Mulch', 'cedar mulch': 'Cedar Mulch', 'black mulch': 'Black Dyed Mulch',
                'brown mulch': 'Brown Dyed Mulch', 'red mulch': 'Red Dyed Mulch', 'Root Mulch': 'Premium Root Mulch', 'root mulch':
                'Premium Root Mulch', 'Hardwood Mulch': 'Premium Hardwood', 'hardwood': 'Premium Hardwood', 'playground mulch': 'Playground Mulch',
                'Woodchips': 'Virgin Woodchips', 'woodchips': 'Virgin Woodchips', 'virgin woodchips': 'Virgin Woodchips', 'top soil': 'Top Soil',
                'compost': 'Compost', 'fill dirt': 'Fill Dirt', '3/4 river rock': '3/4" River Rock', '1.5x3 river rock' : '1.5" x 3" River Rock',
                '3x5 river rock': '3" x 5" River Rock', 'red driveway stone': '3/4" Red Driveway Stone', 'grey driveway stone':
                '3/4" Grey Driveway Stone', 'modified stone': 'Modified Stone 2A', 'stone dust': 'Stone Dust Screenings', 'pea gravel':
                'Pea Gravel', 'sand': 'Sand'}

towns, mats = [], []
for key in deliveryDict:
    towns.append(key)
for key in matDict:
    mats.append(key)
for key in matShortcuts:
    mats.append(key)

lightMats = ['Aged Bark Mulch', 'Cedar Mulch','Red Dyed Mulch', 'Black Dyed Mulch', 'Premium Hardwood', 'Playground Mulch', 'Brown Dyed Mulch',
             'Virgin Woodchips']

def priceCalcStr(mat: str, qt: int, town: str) -> str:
    if mat not in matDict:
        if mat not in matShortcuts: return 'Material not found.'
        else: mat = matShortcuts[mat]
    if town not in towns: return 'Town not found or not available to deliver to.'
    
    matRate, delPrice, tax = matDict[mat], deliveryDict[town], 0.06625

    #Adjusting price per unit for bulk discounts
    if((mat == 'Black Dyed Mulch') | (mat == 'Brown Dyed Mulch')):
        if qt > 19: matRate -= 6
        elif qt > 4: matRate -= 3
    elif(mat == 'Fill Dirt'):
        if qt > 19: matRate -= 5
        elif qt > 4: matRate -= 3
    elif((mat == 'Aged Bark Mulch') | (mat == 'Cedar Mulch') | (mat == 'Red Dyed Mulch') | (mat == 'Premium Root Mulch') | (mat == 'Premium Hardwood') |
        (mat == 'Playground Mulch') | (mat == 'Top Soil') | (mat == 'Compost')):
        if qt > 19: matRate -= 4
        elif qt > 4: matRate -= 2

    #Adjusting delivery price if larger truck
    if qt > 7:
        if mat in lightMats:
            if  qt > 12: delPrice = triDeliveryDict[town]
        else: delPrice = triDeliveryDict[town]

    result = ''
    #User alert if large load, typical max is 23 units
    if qt > 23: result += 'Delivery of this quantity may require multiple truckloads.\nDelivery fee for multiple trucks listed below.\n\n'
    if qt < 3: result += 'This delivery falls below the minimum quantity and will likely be refused.\n'

    matPrice = matRate * qt
    remainingQt = qt-23
    while(remainingQt>0):
        if remainingQt>12 : delPrice += triDeliveryDict[town]
        elif(remainingQt>7) and (mat not in lightMats): delPrice += triDeliveryDict[town]
        else: delPrice += deliveryDict[town]
        remainingQt -= 23
    taxPrice = (matPrice + delPrice) * tax
    total = matPrice + delPrice + taxPrice

    result += f'Material price of ${matRate:0.2f} for {qt} units of {mat} - ${matPrice:0.2f}\n'
    result += f'Delivery price to {town} - ${delPrice:0.2f}\n'
    result += f'Tax cost - ${taxPrice:0.2f}\n\n'
    result += f'TOTAL PRICE - ${total:0.2f}'

    return result

@ui.page('/')
def index():
    txt = ui.label('Quote appears here...').style('white-space: pre-wrap')
    mat = ui.input(label='Material', autocomplete=mats).props('clearable')
    qt = ui.number(label='Quantity')
    town = ui.input(label='Town', autocomplete=towns).props('clearable')
    ui.button('Calculate Price', on_click=lambda: txt.set_text(priceCalcStr(mat.value, qt.value, town.value)))

ui.run(on_air='r0sEOv8WBsxIY3Z3')