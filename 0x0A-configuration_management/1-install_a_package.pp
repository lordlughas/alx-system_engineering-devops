# Using Puppet, install flack from pip3

exec { 'install python packages':
  command => 'pip3 install flask',
  path    => ['/usr/bin/']
}
