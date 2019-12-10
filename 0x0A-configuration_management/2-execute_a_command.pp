# exec shell cmd

exec { 'killmenow':
     command => 'pkill killmenow',
     path => '/usr/bin',
     provider => shell,
     }