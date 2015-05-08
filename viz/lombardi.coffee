
if Meteor.isClient

	Template.info.helpers

	Template.graph.events

	Meteor.startup ->
		sig.initSigmaGraph()

if Meteor.isServer
	Meteor.startup ->


