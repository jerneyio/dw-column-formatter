import sys
import unittest

def first_col_width(row):
  return len(row[0])

def max_col_width(table):  
  return len(max(table, key=first_col_width)[0])

def create_table(string):
  return [x.split(':') for x in string.split('\n') if x.strip() != '']

def rejoin_rows(table, width):
  rows          = []
  right_pad_fmt = '{:' + str(width + 2) + '}'

  for row in table:
    line = ''

    if len(row) == 1:
      line = row[0]
    else:
      line = right_pad_fmt.format(row[0] + ':') + row[1].lstrip()
    
    if len(row) >= 3:
      line = line + ':' + ':'.join(row[2:])

    rows.append(line)

  return rows

def rejoin_lines(rows):
  return '\n'.join(rows)

def run():
  string = sys.stdin.read()

  if string.strip() != '':
    table = create_table(string)
    width = max_col_width(table)
    rows  = rejoin_rows(table, width)
    lines = rejoin_lines(rows)
    
    print(lines)
  
  else:
    print('')

if __name__ == '__main__':
  run()

class Test(unittest.TestCase):
  def setUp(self):
    self.simple_string_input = """
      one: 'one',
      two: 'two',
      three: 'three',
      four: 'four'

    """

    self.simple_table_input = [
      ['      one', " 'one',"],
      ['      two', " 'two',"],
      ['      three', " 'three',"],
      ['      four', " 'four'"]
    ]

    self.table_additional_colons = [
      ['      one', " 'one' as ", "string,"],
      ['      two', " 'two',"],
      ['      three', " 'three',"],
      ['      four', " 'four'"]
    ]

  def test_first_col_width(self):
    self.assertEqual(first_col_width(['foo', 'barbaz']), 3)

  def test_max_col_width(self):
    table = [['foo', 'barbaz'], ['barbaz', 'foo']]

    self.assertEqual(max_col_width(table), 6)

  def test_create_table(self):
    self.assertEqual(create_table(self.simple_string_input), self.simple_table_input)

  def test_rejoin_rows_simple(self):
    expected = [
      "      one:   'one',",
      "      two:   'two',",
      "      three: 'three',",
      "      four:  'four'"
    ]

    self.assertEqual(rejoin_rows(self.simple_table_input, 11), expected)

  def test_rejoin_rows_additional_colons(self):
    expected = [
      "      one:   'one' as :string,",
      "      two:   'two',",
      "      three: 'three',",
      "      four:  'four'"
    ]

    self.assertEqual(rejoin_rows(self.table_additional_colons, 11), expected)