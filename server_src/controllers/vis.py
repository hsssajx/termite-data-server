#!/usr/bin/env python

from core import TermiteCore
from vis.GroupInABox import GroupInABox as GroupInABoxModel
from vis.CovariateChart import CovariateChart as CovariateChartModel

def index():
	core = TermiteCore( request, response )
	return core.GenerateResponse()

def GroupInABox():
	gib = GroupInABoxModel( request, response )
	gib.LoadTopTermsPerTopic()
	gib.LoadTopicCovariance()
	gib.LoadTermFreqs()
	gib.LoadTermCoFreqs()
	gib.LoadTermProbs()
	gib.LoadTermPMI()
	gib.LoadTermSentencePMI()
	return gib.GenerateResponse()

def CovariateChart():
	chart = CovariateChartModel( request, response )
	chart.LoadDocTopicMatrix()
	chart.LoadTopicTopTerms()
	return chart.GenerateResponse()
