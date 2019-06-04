import Base
import CharInfo

def playerlocation():
    if CharInfo.player_info.player_location in ['PC Bedroom', 'Sasha Living Room']:
        Base.pcbedroom()

    elif CharInfo.player_info.player_location in ["Sasha First Dialogue", 'Sasha Second Dialogue', 'Holly Cafe']: \
         Base.hallway()

    elif CharInfo.player_info.player_location in ['Jacob Kitchen Dialogue']:
        Base.entranceway()

    elif CharInfo.player_info.player_location in ['Park Walk']:
        Base.sycamore_park.lakepark()

    elif CharInfo.player_info.player_location in ['Festival Start']:
        import Festival
        Festival.festival_area.festival_entrance()