**Start application**

| AS A | Player |  |
|------|--------|--|
| I WANT TO | Start the game |  |
| 1 | GIVEN | The application exits on the machine |
|  | WHEN | Application is started |
|  | THEN | The game menu appears |

**START A NEW GAME**

| AS A | Player |  |
|------|--------|--|
| I WANT TO | Start a new game |  |
| 1 | GIVEN | The game menu is responsive |
|  | WHEN | I click on the button for starting a new game |
|  | THEN | The new game session should begin |

**SETTING THE ZONES**

| AS A | Player |  |
|------|--------|--|
| I WANT TO | Set the zones of the game at the beginning |  |
| 1 | GIVEN | The new game starts |
|  | WHEN | I click on the Zones dropdown menu appears and I select the place where I would like each zone to be |
|  | THEN | The zones will be set |

**POPULATING THE ZONES**

| AS A | Player |  |
|------|--------|--|
| I WANT TO | Populate the selected zone |  |
| 1 | GIVEN | The residential zones are selected and I have enough funds |
|  | WHEN | I click on type of building I want to build |
|  | THEN | The selected type of building is built |
| 2 | GIVEN | The industrial zones are selected and I don’t have enough funds |
|  | WHEN | I click on the type of building I want to build |
|  | THEN | The selected type of building is built |
| 3 | GIVEN | The service zones are selected and I have enough funds |
|  | WHEN | I click on the type of building I want to build |
|  | THEN | The selected type of building is built |
|  |  |  |
| AS A | Player |  |
| I WANT TO | Reclassify the selected zone |  |
| 1 | GIVEN | The previously built zone hasn’t been built on |
|  | WHEN | I click the Zone -> Change |
|  | THEN | The zone will change and I will be partially refunded |

**BUILDING CITY**

| AS A | Player |  |
|------|--------|--|
| I WANT TO | Build a city |  |
| 1 | GIVEN | Player has chosen the correct zone and has sufficient funds and the zone is “road accessible” |
|  | WHEN | I click BUILD -> Choose available buildings |
|  | THEN | The building is built and my money is withdrawn |
| 2 | GIVEN | Player has chosen the correct zone but doesn’t have sufficient funds for building the building |
|  | WHEN | I click BUILD -> Choose available buildings |
|  | THEN | The building is not being built |
| 3 | GIVEN | The player wants to build service buildings in non-zone fields with sufficient funds |
|  | WHEN | I click BUILD -> Choose available buildings |
|  | THEN | The building is being built |
| 4 | GIVEN | The player wants to build service buildings in zoned fields with sufficient funds |
|  | WHEN | I click BUILD -> Choose available buildings |
|  | THEN | The building is not being built |
| 5 | GIVEN | The player wants to build service buildings in non-zoned fields with insufficient funds |
|  | WHEN | I click BUILD -> Choose available buildings |
|  | THEN | The building is not being built |
| 6 | GIVEN | The player wants to demolish the service building |
|  | WHEN | I click BUILD -> Destroy -> Click on building |
|  | THEN | The building is demolished and money is partial reimbursed |
| 7 | GIVEN | The player wants to build roads on the zoned or non-zoned spaces and has enough funds |
|  | WHEN | I click BUILD -> Road |
|  | THEN | The road will be built and money will be deducted |
| 8 | GIVEN | The player wants to build roads on the zoned or non-zoned spaces and doesn’t have enough funds |
|  | WHEN | I click BUILD -> Road |
|  | THEN | The road won't be built |
| 9 | GIVEN | The player wants to demolish the road which destroys connection |
|  | WHEN | I click BUILD -> Demolish -> Road |
|  | THEN | The road won't be demolished |
| 10 | GIVEN | The player wants to build a police station on general zone and has sufficient funds|
|  | WHEN | I click BUILD -> Police station|
|  | THEN | The police station will be built  |
| 11 | GIVEN | The player wants to build a stadium on general zone and has sufficient funds|
|  | WHEN | I click BUILD -> stadium|
|  | THEN | The stadium will be built  |

**Managing people**

| AS A | Player |  |
|------|--------|--|
| I WANT TO | I want my citizens to be satisfied |  |
| 1 | GIVEN | Player chooses a zone |
|  | WHEN | I click on the zone I want to select |
|  | THEN | In the menu part we will have satisfaction rate in percent |

**Expenses**

| AS A | Player |  |
|------|--------|--|
| I WANT TO | I want manage my expenses and income |  |
| 1 | GIVEN | I want as much people as possible |
|  | WHEN | I build more residential spaces |
|  | THEN | I can earn more from taxes |

**Changes**

| AS A | Player |  |
|------|--------|--|
| I WANT TO | I want to change default city name |  |
| 1 | GIVEN | I have started the game|
|  | WHEN | I click on the Menu -> System -> City name |
|  | THEN |The name of the city will be changed|
| AS A | Player |  |
| I WANT TO | I want to change default citizen tax |  |
| 1 | GIVEN | I have started the game and have citizens who work|
|  | WHEN | I click on the Menu -> System -> Citizen tax |
|  | THEN |The citizen tax is changed|
| AS A | Player |  |
| I WANT TO | Change the speed of the game |  |
| 1 | GIVEN | I have started the game|
|  | WHEN | I click on the Menu -> System -> Click on the desired speed|
|  | THEN |The time will elapse faster|



**Exit the game**

| AS A | Player |  |
|------|--------|--|
| I WANT TO | I want to exit the game |  |
| 1 | GIVEN | I have played enough |
|  | WHEN | I click on the Menu -> Exit |
|  | THEN | I will be back in the starting menu |

**Features : Forest, Disaster**

| AS A | Player |  |
|------|--------|--|
| I WANT TO | plant as much forests as possible |  |
| 1 | GIVEN | I want to plant it on general field |
|  | WHEN | I click BUILD -> FOREST |
|  | THEN | The forest will be planted and quality will be improved |

| AS A | Player |  |
|------|--------|--|
| I WANT TO | Create a disaster effect |  |
| 1 | GIVEN | I have more than 0 people in my city |
|  | WHEN | I click DISASTER |
|  | THEN | The population will decrease and some building will be demolished |

