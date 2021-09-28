from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."
  
    def build( self ):
        "Create custom topo."
     
        # Add hosts and switches
        host1Switch1 = self.addHost( 'h1' )
        host2Switch1 = self.addHost( 'h2' )
        host1Switch2 = self.addHost( 'h3' )
        host2Switch2 = self.addHost( 'h4' )
        host1Switch3 = self.addHost( 'h5' )
        host2Switch3 = self.addHost( 'h6' )
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        switch3 = self.addSwitch( 's3' )

        # Add links
        self.addLink( host1Switch1, switch1 )
        self.addLink( host2Switch1, switch1 )
        self.addLink( host1Switch2, switch2 )
        self.addLink( host2Switch2, switch2 )
        self.addLink( host1Switch3, switch3 )
        self.addLink( host2Switch3, switch3 )
        self.addLink( switch1, switch2 )
        self.addLink( switch2, switch3 )
 
topos = { 'mytopo': ( lambda: MyTopo() ) }
