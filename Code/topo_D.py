"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined m
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        #h1 = self.addHost( 'h1' )
        #h2 = self.addHost( 'h2' )
        #h3 = self.addHost( 'h3 ')
        #h4 = self.addHost( 'h4 ')
        # h5 = self.addHost( 'h5 ')

        h1 = self.addHost( 'h1', ip='10.0.0.1/16')
        h2 = self.addHost( 'h2', ip='10.0.0.2/16')
        h3 = self.addHost( 'h3', ip='10.0.0.3/16')
        h4 = self.addHost( 'h4', ip='10.0.1.2/16')
        h5 = self.addHost( 'h5', ip='10.0.1.3/16')

        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        

        # Add links
        self.addLink( h1, s1 )
        self.addLink( h2, s1 )
        self.addLink( h3, s1 )

        self.addLink( s1, s2 )
        self.addLink( s2, s3 )

        self.addLink( h4, s3 )
        self.addLink( h5, s3 )



topos = { 'mytopo': ( lambda: MyTopo() ) }



