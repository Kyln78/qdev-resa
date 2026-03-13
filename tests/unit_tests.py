import unittest
from resa.resa import *

class bookMeetingRoomUnitTests(unittest.TestCase):
  def test_small_room(self):
    self.assertEqual(bookMeetingRoom(5), Room.SMALL)
    self.assertEqual(bookMeetingRoom(10), Room.SMALL)

  def test_medium_room(self):
    self.assertEqual(bookMeetingRoom(18), Room.MEDIUM)

  def test_large_room(self):
    self.assertEqual(bookMeetingRoom(46), Room.LARGE)

  def test_refused_room(self):
    self.assertEqual(bookMeetingRoom(60),  Room.REFUSE)

  def test_erreur_room(self):

    self.assertRaises(ValueError, bookMeetingRoom, 0)


if __name__ == '__main__':
  unittest.main()
