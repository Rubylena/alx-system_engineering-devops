# using puppet, install flask from pip3

$value = 'flask'
package { 'flask':
  name = $value,
  ensure   => '2.1.0',
  provider => 'pip3',
}
