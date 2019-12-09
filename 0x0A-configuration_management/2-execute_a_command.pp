exec { 'killmenow':
     command => 'pkill',
     path => '.',
     provider => shell,
     }