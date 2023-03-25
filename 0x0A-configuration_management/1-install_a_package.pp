# Using Puppet, install flack from pip3

exec { 'install python packages':
  command => 'pip3 install flask',
  ensure  => '2.1.0',
  path    => ['/usr/bin/']
}
