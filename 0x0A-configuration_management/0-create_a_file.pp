# using puppet to create a file in /tmp

file { '0-create_a_file':
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
