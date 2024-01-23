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
      (121.2 + 120.48) / 2)
    print("Actual result:", actual_result)
    print("Expected result:", expected_result)
    actual_result1 = getDataPoint(quotes[1])
    expected_result1 = (
      quotes[1]['stock'],
      float(quotes[1]['top_bid']['price']),
      float(quotes[1]['top_ask']['price']),
      (117.87 + 121.68) / 2)
    print("Actual result1:", actual_result1)
    print("Expected result1:", expected_result1)
    self.assertEqual(actual_result, expected_result, expected_result1)


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
      (120.48 + 119.2) / 2)
    print("Actual result:", actual_result)
    print("Expected result:", expected_result)
    actual_result1 = getDataPoint(quotes[1])
    expected_result1 = (
      quotes[1]['stock'],
      float(quotes[1]['top_bid']['price']),
      float(quotes[1]['top_ask']['price']),
      (117.87 + 121.68) / 2)
    print("Actual result1:", actual_result1)
    print("Expected result1:", expected_result1)
    self.assertEqual(actual_result, expected_result, expected_result1)


""" ------------ Add more unit tests ------------ """


if __name__ == '__main__':
    unittest.main()