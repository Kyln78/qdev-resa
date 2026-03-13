from enum import Enum

class Room(Enum):
  REFUSE = 0
  SMALL = 1
  MEDIUM = 2
  LARGE = 3

  def __str__(self):
    if self == Room.LARGE:
      return "Large"
    if self == Room.MEDIUM:
      return "Medium"
    if self == Room.SMALL:
      return "Small"

    return "Refused"

def bookMeetingRoom(participants):
  return Room.REFUSE
