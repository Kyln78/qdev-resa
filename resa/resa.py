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
    if type(participants) != int:
        raise TypeError("n'est pas un entier")
    if 1 <= participants <= 10:
        return Room.SMALL
    if 11 <= participants <= 30:
        return Room.MEDIUM
    if 31 <= participants <= 50:
        return Room.LARGE
    if participants > 50 :
        return Room.REFUSE
    if participants <1:
        raise ValueError("Indisponible")

    return Room.REFUSE
