import pygame as pg
import pytest
import sys
sys.path.append('./GUIGame')  # importing sys library
sys.path.append('./Zones')
sys.path.append('./Buildings')
sys.path.append('./my_game')
# from zone import general, industrial, residential, service
from Field import Field

def test_field_initialization():
    field = Field(0, 0, 50)
    assert field.x == 0
    assert field.y == 0
    assert field.size == 50
    assert field.grid_pos is None
    assert field.color == (86, 148, 70)
    assert field.building == ""
    assert field.img is None
    assert field.zone is None
    assert not field.road
    assert not field.selected
    assert field.rect == pg.Rect(0, 0, 50, 50)
    assert field.id is None
    assert field.image_rect is None

def test_getX():
    field = Field(10, 20, 50)
    assert field.getX() == 10

def test_connectsTo():
    field = Field(0, 0, 50)
    field.road = True
    reachable_fields = field.connectsTo()
    assert len(reachable_fields) == 4
    assert (0, 55) in reachable_fields
    assert (0, -55) in reachable_fields
    assert (55, 0) in reachable_fields
    assert (-55, 0) in reachable_fields

# def test_destructible():
#     field = Field(0, 0, 50)
#     field.road = True
#     other_fields = [
#         Field(0, 50, 50),
#         Field(0, -50, 50),
#         Field(50, 0, 50),
#         Field(-50, 0, 50),
#     ]
#     assert field.destructible(other_fields)

#     field.zone = Zone()  
#     assert not field.destructible(other_fields)

#     field.zone = None
#     other_fields[0].road = True
#     assert not field.destructible(other_fields)

#     other_fields[0].road = False
#     other_fields[1].road = False
#     assert not field.destructible(other_fields)

#     other_fields[2].zone = Zone(typ="residential")
#     assert not field.destructible(other_fields)

# def test_set_zone():
#     field = Field(0, 0, 50)
#     zone = Zone()  # Assuming you have the Zone class defined
#     field.set_zone(zone)
#     assert field.zone == zone

def test_set_road():
    field = Field(0, 0, 50)
    field.set_road()
    assert field.road




def test_initialization():
    field = Field(10, 20, 60)
    assert field.x == 10
    assert field.y == 20
    assert field.size == 60
    assert field.grid_pos is None
    assert field.color == (86, 148, 70)
    assert field.building == ""
    assert field.img is None
    assert field.zone is None
    assert not field.road
    assert not field.selected
    assert field.rect == pg.Rect(10, 20, 60, 60)
    assert field.id is None
    assert field.image_rect is None

def test_getXY():
    field = Field(50, 100, 70)
    assert field.getX() == 50

def test_Road_To():
    field = Field(0, 0, 80)
    field.road = True
    reachable_fields = field.connectsTo()
    assert len(reachable_fields) == 4
    assert (0, 55) in reachable_fields
    
def test_set_road():
    field = Field(0, 0, 90)
    field.set_road()
    assert field.road

class Zone:
    def __init__(self, typ="general"):
        self.typ = typ
        



# Run the tests
pytest.main()

