import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count(self):
        result = hw1.vowel_count("hi there")
        expected = 3
        self.assertEqual(result, expected)

    def test_vowel_count_2(self):
        result = hw1.vowel_count("I love computer science")
        expected = 9
        self.assertEqual(result, expected)

    # Part 2
    def test_short_lists(self):
        result = hw1.short_lists([[4, 5, 6, 5], [5], [6, 5]])
        expected = [[6,5]]
        self.assertEqual(result, expected)

    def test_short_lists_2(self):
        result = hw1.short_lists([[4, 500], [5, 8], [6, 5, 6]])
        expected = [[4, 500], [5, 8]]
        self.assertEqual(result, expected)

    # Part 3
    def test_ascending_pairs(self):
        expected = [[4, 5,], [4, 7], [4, 8], [5, 6, 4]]
        result = hw1.ascending_pairs([[4, 5], [7, 4], [4, 8], [5, 6, 4]])
        self.assertEqual(result, expected)

    def test_ascending_pairs_2(self):
        expected = [[5, 5], [2, 4], [55, 6, 4]]
        result = hw1.ascending_pairs([[5, 5], [4, 2], [55, 6, 4]])
        self.assertEqual(result, expected)

    # Part 4
    def test_add_prices(self):
        money1 = data.Price(3, 49)
        money2 = data.Price(400, 560)
        expected = data.Price(409, 9)
        result = hw1.add_prices(money1, money2)
        self.assertEqual(expected, result)

    def test_add_prices2(self):
        money1 = data.Price(5, 40)
        money2 = data.Price(5, 1060)
        expected = data.Price(21,0)
        result = hw1.add_prices(money1, money2)
        self.assertEqual(expected, result)

    # Part 5
    def test_rectangle_area(self):
        point1left = data.Point(0, 5)
        point1right = data.Point(4, 0)
        therectangle = data.Rectangle(point1left, point1right)
        result = hw1.rectangle_area(therectangle)
        expected = 20
        self.assertEqual(result, expected)

    def test_rectangle_area2(self):
        point1left = data.Point(15, 9)
        point1right = data.Point(30, 0)
        therectangle = data.Rectangle(point1left, point1right)
        result = hw1.rectangle_area(therectangle)
        expected = 135
        self.assertEqual(result, expected)

    # Part 6
    def test_books_by_author(self):
        book1 = data.Book(["a", "b", "c"], "title1")
        book2 = data.Book(["a", "c", "d"], "title2")
        result = hw1.books_by_author("a", [book1, book2])
        expected =[data.Book(['a', 'b', 'c'], 'title1'), data.Book(['a', 'c', 'd'], 'title2')]
        self.assertEqual(result, expected)

    def test_books_by_author_2(self):
        book1 = data.Book(["john", "annika", "cameron"], "title1")
        book2 = data.Book(["elle", "annika", "dillan"], "title2")
        book3 = data.Book(["elle", "annika", "sophie"], "title3")
        book4 = data.Book(["sophie", "elle"], "title4")
        result = hw1.books_by_author("annika", [book1, book2, book3, book4])
        expected = [data.Book(['john', 'annika', 'cameron'], 'title1'), data.Book(['elle', 'annika', 'dillan'], 'title2'), data.Book(['elle', 'annika', 'sophie'], 'title3')]
        self.assertEqual(result, expected)

    # Part 7
    def test_circle_bound(self):
        Point1 = data.Point(0, 5)
        Point2 = data.Point(10, 0)
        result = hw1.circle_bound(data.Rectangle(Point1, Point2))
        centerpoint = data.Point(5, 2.5)
        expected = data.Circle(centerpoint, 2.5)
        self.assertEqual(result, expected)

    def test_circle_bound2(self):
        Point1 = data.Point(5, 20)
        Point2 = data.Point(10, 0)
        result = hw1.circle_bound(data.Rectangle(Point1, Point2))
        expected = data.Circle(data.Point(7.5, 10), 2.5)
        self.assertEqual(result, expected)

    # Part 8
    def test_below_pay_average(self):
        employee1 = data.Employee("annika", 70.5)
        employee2 = data.Employee("Joe", 15)
        employee3 = data.Employee("Cami", 40)
        result = hw1.below_pay_average([employee1, employee2, employee3])
        expected = ['Joe', 'Cami']

    def test_below_pay_average_2(self):
        employee1 = data.Employee("Tonya", 3.5)
        employee2 = data.Employee("Kate", 60)
        employee3 = data.Employee("Zoe", 20)
        employee4 = data.Employee("Ginny", 35)
        result = hw1.below_pay_average([employee1, employee2, employee3, employee4])
        expected = ['Tonya', 'Zoe', 'Ginny']




if __name__ == '__main__':
    unittest.main()
