import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    actual_result = getDataPoint(quotes[0])
    expected_result = (
      quotes[0]['stock'],
      float(quotes[0]['top_bid']['price']),
      float(quotes[0]['top_ask']['price']),
      (121.2 + 120.48) / 2
    )

    print("Actual result:", actual_result)
    print("Expected result:", expected_result)

    self.assertEqual(actual_result, expected_result)

  #self.assertEqual(getDataPoint(quotes[0]), (quotes[0]['stock'], float(quotes[0]['top_bid']['price']), float(quotes[0]['top_ask']['price']), (121.2 + 120.48) /2))

  # self.assertEqual(getDataPoint(quotes[1]), (quotes[1]['stock'], quotes[1]['top_bid']['price'], quotes[1]['top_ask']['price'], (quotes[1]['top_bid']['price'] + quotes[1]['top_ask']['price']) / 2))
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    actual_result = getDataPoint(quotes[0])
    expected_result = (
      quotes[0]['stock'],
      float(quotes[0]['top_bid']['price']),
      float(quotes[0]['top_ask']['price']),
      (120.48 + 119.2) / 2
    )

    print("Actual result:", actual_result)
    print("Expected result:", expected_result)

    self.assertEqual(actual_result, expected_result)

    # self.assertEqual(getDataPoint(quotes[0]), (quotes[0]['stock'], quotes[0]['top_bid']['price'], quotes[0]['top_ask']['price'],(quotes[0]['top_bid']['price'] + quotes[0]['top_ask']['price']) / 2))
    # self.assertEqual(getDataPoint(quotes[1]), (quotes[1]['stock'], quotes[1]['top_bid']['price'], quotes[1]['top_ask']['price'],(quotes[1]['top_bid']['price'] + quotes[1]['top_ask']['price']) / 2))
  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
