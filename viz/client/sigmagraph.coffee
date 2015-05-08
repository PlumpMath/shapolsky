@sig = {}

sig.initSigmaGraph = (graphData) ->
	g =
		nodes: []
		edges: []

	N = 300

	for i in [1 .. N]
		console.log i
		g.nodes.push $.extend({}, 
			color: "#555599"
			size: Math.random()
			label: "Node " + i
			x: Math.cos(2 * i * Math.PI / N)
			y: Math.sin(2 * i * Math.PI / N)
			id: i.toString()
		)

	for i in [1 .. N]
		console.log "oh, anedge"
		g.edges.push $.extend({}, 
			source: _.sample(g.nodes).id
			target: _.sample(g.nodes).id
			id: i.toString() 
		)

	console.log g
	sig.s = new sigma(
		graph: g
		container: "sigmagraph"
		settings:
			drawEdges: true
	)
	
	# Start the ForceAtlas2 algorithm:
	fa2config =
		gravity: 5.1
		slowDown: 0.2
		startingIterations: 1
		edgeWeightInfluence: 1
		linLogMode: true
		strongGravityMode: false

	sig.s.startForceAtlas2 fa2config

	return
