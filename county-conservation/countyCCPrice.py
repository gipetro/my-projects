from nicegui import ui

deliveryDict = {'Absecon': 185, 'Alloway': 120, 'Atco': 135, 'Atlantic City': 210, 'Audubon': 100, 'Audubon Park': 100, 'Avalon': 175,
                'Barrington': 100, 'Bass River Township': 200, 'Bellmawr': 100, 'Berlin': 100, 'Berlin Township': 100,
                'Beverly': 160, 'Blackwood': 70, 'Blue Anchor': 110, 'Bordentown': 170, 'Bordentown Township': 170, 'Bridgeton': 160,
                'Brigatine': 210, 'Brooklawn': 90, 'Buena': 105, 'Buena Vista': 185, 'Burlington': 160, 'Burlington Township': 160,
                'Camden': 210, 'Cape May': 200, 'Cape May Courthouse': 200, 'Cape May Point': 210, 'Carneys Point': 135, 'Cherry Hill': 135,
                'Chesilhurst': 110, 'Chesterfield Township': 170, 'Cinnaminson Township': 140, 'Clayton': 70, 'Clarksboro': 100, 'Clementon': 90,
                'Collingswood': 100, 'Commercial Township': 155, 'Corbin City': 190, 'Deerfield Township': 90, 'Delanco': 135, 'Delran': 150,
                'Dennis': 170, 'Deptford': 90, 'Downe Township': 155, 'East Greenwich Township': 90, 'Eastampton': 160, 'Edgewater Park': 160,
                'Egg Harbor City': 190, 'Egg Harbor Township': 190, 'Elk Township': 70, 'Elmer': 95, 'Elsinboro': 150, 'Estell Manor': 190,
                'Evesham': 150, 'Fairfield Township': 160, 'Fieldsboro': 165, 'Florence Township': 160, 'Folsom': 185, 'Franklin Township': 70,
                'Galloway': 185, 'Gibbsboro': 100, 'Gibbstown': 90, 'Glassboro': 80, 'Glendora': 95, 'Gloucester City': 95, 'Gloucester Township': 80,
                'Greenwich Township': 160, 'Haddon Heights': 90, 'Haddon Township': 105, 'Haddonfield': 105, 'Hainesport': 160,
                'Hamilton Township': 185, 'Hammonton': 185, 'Harrison Township': 105, 'Hi-Nella': 90, 'Hopewell Township': 160,
                'Laurel Springs': 90, 'Lawnside': 95, 'Lawrence Township': 160, 'Lindenwold': 100, 'Linwood': 185, 'Logan Township': 105,
                'Longwood': 210, 'Lower': 197.5, 'Lower Alloways Creek': 190, 'Lumberton': 160, 'Magnolia': 90, 'Mannington': 110,
                'Mansfield': 165, 'Mantua Township': 80, 'Maple Shade': 110, 'Margate': 210, 'Marlton': 170, 'Maurice River': 160,
                'Medford': 160, 'Medford Lakes': 160, 'Medford Township': 160, 'Merchantville': 110, 'Mickleton': 100, 'Middle': 170,
                'Millville': 80, 'Monroeville': 90, 'Moorestown': 160, 'Mount Ephraim': 90, 'Mount Holly': 135, 'Mount Laurel': 150,
                'Mount Royal': 100, 'Mullica Hill': 100, 'Mullica Township': 185, 'National Park': 90, 'New Hanover': 160, 'Newfield': 90,
                'North Hanover': 210, 'North Wildwood': 200, 'Northfield': 190, 'Oaklyn': 90, 'Ocean City': 210, 'Oldmans': 105, 'Palmyra': 135,
                'Paulsboro': 90, 'Pedricktown': 105, 'Pemberton': 160, 'Penns Grove': 135, 'Pennsauken Township': 110, 'Pennsville': 150,
                'Pilesgrove': 105, 'Pine Hill': 95, 'Pine Valley': 95, 'Pitman': 90, 'Pittsgrove': 120, 'Pleasantville': 190, 'Port Republic': 200,
                'Quinton': 120, 'Riverside': 150, 'Riverton': 150, 'Runnemede': 95, 'Salem': 125, 'Sea Isle': 160, 'Sewell': 70, 'Shamong': 150,
                'Shiloh': 160, 'Sicklerville': 100, 'Somerdale': 90, 'Somers Point': 195, 'South Harrison': 90, 'Southampton': 150, 'Springfield': 165,
                'Stone Harbor': 175, 'Stow Creek Township': 160, 'Stratford': 90, 'Swedesboro': 90, 'Tabernacle': 150, 'Tavistock': 105,
                'Tuckerton': 190, 'Turnersville': 70, 'Upper': 165, 'Upper Deerfield Township': 155, 'Upper Pittsgrove': 110, 'Ventnor City': 210,
                'Vincetown': 150, 'Vineland': 80, 'Voorhees Township': 100, 'Washington Township': 70, 'Waterford Township': 110, 'Wenonah': 80,
                'West Cape May': 210, 'West Deptford': 105, 'West Wildwood': 190, 'Westampton Township': 155, 'Westville': 105,
                'Weymouth Township': 190, 'Wildwood': 190, 'Wildwood Crest': 190, 'Williamstown': 100, 'Willingboro': 160, 'Winslow Township': 110,
                'Woodbine': 170, 'Woodbury': 90, 'Woodbury Heights': 85, 'Woodland Township': 185, 'Woodlynne': 105, 'Woodstown': 105}

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
        if((mat == 'Aged Bark Mulch') | (mat == 'Cedar Mulch') | (mat == 'Red Dyed Mulch') | (mat == 'Black Dyed Mulch') |
            (mat == 'Premium Hardwood') | (mat == 'Playground Mulch') | (mat == 'Brown Dyed Mulch') | (mat == 'Virgin Woodchips')):
            if  qt > 12: delPrice *= 2
        else: delPrice *= 2

    result = ''
    #User alert if large load, typical max is 23 units
    if qt > 23: result += 'Delivery of this quantity may require multiple truckloads.\nMultiply delivery price as needed\n'

    matPrice = matRate * qt
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