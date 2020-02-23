var svg = d3.select('svg')
	.attr({
		'width': full_width + margin.left + margin.right,
		'height': h + margin.top + margin.bottom
	})
	.append('g')
	.attr({
		'transform': 'translate(' + margin.left + ',' + margin.top + ')',
		'width': full_width,
		'height': h
	});

var corrplot = svg.append('g')
	.attr({
		'id': 'corrplot',
		'transform': 'translate(' + w_smaller / 2 + ',' + h_smaller / 2 + ')',
		"width": w - w_smaller,
		"height": h - h_smaller
	});

var scatprompt = svg.append('g')
	.attr({
		'id': 'scatprompt',
		'transform': 'translate(' + (w + pad) + ',' + h/2 + ')'
	});

var scatterplot1 = svg.append('g')
	.attr({
		'id': 'scatterplot1',
		'transform': 'translate(' + (w + pad) + ',0)'
	});

var scatterplot2 = svg.append('g')
	.attr({
		'id': 'scatterplot2',
		'transform': 'translate(' + (w + pad) + ',' + (h+h_btw_scat)/2 + ')'
	});

var drawScatter = function(col, row, whichrawdat) {
	console.log('Showing column ' + col + ', row ' + row);

	d3.selectAll('.points').remove();
	d3.selectAll('.axis').remove();
	d3.selectAll('.scatterlabel').remove();
	scatprompt.selectAll('g').remove();

	var xScale1 = d3.scale.linear()
		.domain(d3.extent((is_X_Y ? dat1_Y : dat1).dat[col]))
		.range([0, w_scat]);
	var yScale1 = d3.scale.linear()
		.domain(d3.extent((is_X_Y ? dat1_X : dat1).dat[row]))
		.range([two ? (h-h_btw_scat)/2 : h, 0]);
	var xAxis1 = d3.svg.axis()
		.scale(xScale1)
		.orient('bottom')
		.ticks(num_ticks)
	var yAxis1 = d3.svg.axis()
		.scale(yScale1)
		.orient('left')
		.ticks(num_ticks);                
	if (two){
		var xScale2 = d3.scale.linear()
			.domain(d3.extent((is_X_Y ? dat2_Y : dat2).dat[col]))
			.range([0, w_scat]);
		var yScale2 = d3.scale.linear()
			.domain(d3.extent((is_X_Y ? dat2_X : dat2).dat[row]))
			.range([(h-h_btw_scat)/2, 0]);
		var xAxis2 = d3.svg.axis()
			.scale(xScale2)
			.orient('bottom')
			.ticks(num_ticks);

		var yAxis2 = d3.svg.axis()
			.scale(yScale2)
			.orient('left').
			ticks(num_ticks);
	}

	scatterplot1.append('g')
	.append('text')
	.text('Scatter plot, '+window[whichrawdat+"_name"]+', raw '+ (((!is_X_Y) && col === row) ? 1 : Math.round(window["cor_"+cortype+"_raw_"+whichrawdat+"_mat"][col*nvar_X+row].value*1000)/1000))
	.attr({
		'class': 'scatplottitle',
		'x': w_scat/2,
		'y': -labelsize,
		'dominant-baseline': 'middle',
		'text-anchor': 'middle'
	})
	.style("font-size", labelsize+"px");

	if (two){
		scatterplot2.append('g')
		.append('text')
		.text('Scatter plot, '+window["second_name"]+', raw ' + (((!is_X_Y) && col === row) ? 1 : Math.round(window["cor_"+cortype+"_raw_second_mat"][col*nvar_X+row].value*1000)/1000))
		.attr({
			'class': 'scatplottitle',
			'x': w_scat/2,
			'y': -labelsize,
			'dominant-baseline': 'middle',
			'text-anchor': 'middle'
		})
		.style("font-size", labelsize+"px");
	}

	scatterplot1.append('g')
	.attr('class', 'points')
	.selectAll('empty')
	.data(d3.range(nind1))
	.enter().append('circle')
	.attr({
		'class': 'point',
		'cx': function(d) {
			return xScale1((is_X_Y ? dat1_Y : dat1).dat[col][d]);
		},
		'cy': function(d) {
			return yScale1((is_X_Y ? dat1_X : dat1).dat[row][d]);
		},
		'r': 5,
		'stroke': 'none',
		'fill': 'black'
	});

	console.log("Showing scatter plot of "+window[whichrawdat+"_name"])

	scatterplot1.append('g')
	.attr('class', 'x axis')
	.attr('transform', 'translate(' + 0 + ',' + (two ? (h-h_btw_scat)/2 : h) + ')')
	.call(xAxis1);

	scatterplot1.append('g')
	.attr('class', 'y axis')
	.attr('transform', 'translate(' + 0 + ', 0)')
	.call(yAxis1);

	scatterplot1.append('g').append('text')
	.text((is_X_Y ? vars_Y : vars)[col])
	.attr({
		'class': 'scatterlabel',
		'x': w_scat/2,
		'y': h + 1.5*labelsize,
		'text-anchor': 'middle',
		'dominant-baseline': 'middle'
	})
	.style("font-size", labelsize+"px");

	scatterplot1.append('g').append('text')
	.text((is_X_Y ? vars_X : vars)[row])
	.attr({
		'class': 'scatterlabel',
		'transform': 'translate(' + (w_scat+labelsize) + ',' + (h/2) + ')rotate(270)',
		'dominant-baseline': 'middle',
		'text-anchor': 'middle'
	})
	.style("font-size", labelsize+"px");

	if (two){
		scatterplot2.append('g')
		.attr('class', 'points')
		.selectAll('empty')
		.data(d3.range(nind2))
		.enter().append('circle')
		.attr({
			'class': 'point',
			'cx': function(d) {
				return xScale2((is_X_Y ? dat2_Y : dat2).dat[col][d]);
			},
			'cy': function(d) {
				return yScale2((is_X_Y ? dat2_X : dat2).dat[row][d]);
			},
			'r': 5,
			'stroke': 'none',
			'fill': 'black'
		});
		
		console.log("Showing scatter plot of "+second_name)
		scatterplot2.append('g')
		.attr('class', 'x axis')
		.attr('transform', 'translate(' + 0 + ',' + (h-h_btw_scat)/2  + ')')
		.call(xAxis2);

		scatterplot2.append('g')
		.attr('class', 'y axis')
		.attr('transform', 'translate(' + 0 + ', 0)')
		.call(yAxis2);
	}
}; // Definition of drawScatter


function drawD3(cortype, testtype, two, datfile, whichrawdat="first"){

	corrplot.selectAll('g').remove();
	scatterplot1.selectAll('g').remove();
	scatterplot2.selectAll('g').remove();
	console.log("Showing "+datfile);

	corrplot.append('g').append('rect')
		.attr({
			'class': 'corrbox',
			'x': 0, 'y': 0,
			'width': w - w_smaller,
			'height': h - h_smaller,
			'fill': 'none',
			'stroke': 'black',
			'stroke-dasharray': '20,20',
			'stroke-width': '1'
		});

	if (two){
		if (is_X_Y) {
			dat1_X = dat_first_X;
			dat1_Y = dat_first_Y;
			dat2_X = dat_second_X;
			dat2_Y = dat_second_Y;
		} else {
			dat1 = dat_first;
			dat2 = dat_second;
		}
		nind1 = nind_first;
		nind2 = nind_second;
		whichrawdat="first";
	} else {
		if (is_X_Y) {
			dat1_X = window["dat_"+whichrawdat+"_X"];
			dat1_Y = window["dat_"+whichrawdat+"_Y"];
		} else {
			dat1 = window["dat_"+whichrawdat]
		}
		nind1 = window["nind_"+whichrawdat];
	}
	corrmat = window[datfile+"_mat"];

	/*if (typeof window[datfile] === 'undefined'){
		 corrplot.append('g').append('text')
			.text(((!two || cortype !== "pearson") && testtype === "cai") ? "Cai tests only supported for two-sample pearson correlations." : "Data not available.")
			.attr({
				'class': 'scatterlabel',
				'x': (w-w_smaller)/2,
				'y': (h-h_smaller)/2,
				'text-anchor': 'middle',
				'dominant-baseline': 'middle'
			})
			.style("font-size", labelsize+"px");
		scatprompt.selectAll('g').remove();
		return null
	}*/

	scatprompt.append('g').append('text')
	.attr('dy', '-2em')
	.text('Click on an entry of the')
	.style("font-size", labelsize+"px");
	scatprompt.append('g').append('text')
	.attr('dy', '0em')
	.text('correlation matrix on the left')
	.style("font-size", labelsize+"px");
	scatprompt.append('g').append('text')
	.attr('dy', '2em')
	.text('to explore the scatter plot(s).')
	.style("font-size", labelsize+"px");

	corrplot.append('g').append('text')
	.text((two ? 'Differential correlation matrix' : 'Correlation matrix') + ": " + (Math.round(window["prop_"+datfile]*100)/100) + "% nonzero")
	.attr({
		'class': 'corrplottitle',
		'x': w/2 - w_smaller/2,
		'y': -margin.top/2 - h_smaller/2,
		'dominant-baseline': 'middle',
		'text-anchor': 'middle'
	})
	.style("font-size", labelsize+"px");

	var corXscale = d3.scale.ordinal().rangeRoundBands([0,w - w_smaller]),
		corYscale = d3.scale.ordinal().rangeRoundBands([0,h - h_smaller]),
		corColScale = d3.scale.linear().domain([-1,0,1]).range(['crimson','white','slateblue']);
	var corRscale = d3.scale.sqrt().domain([0,1]);
		corXscale.domain(d3.range(nvar_Y));
		corYscale.domain(d3.range(nvar_X));
		corRscale.range([0,(0.5+0.2*two)*corXscale.rangeBand()]); ////// corXscale.rangeBand() == corYscale.rangeBand() anyways

	var cells = corrplot.append('g')
		.attr('id', 'cells')
		.selectAll('empty')
		.data(corrmat)
		.enter().append('g')
		.attr({
			'class': 'cell'
		})
		.style('pointer-events', 'all');

	var rects = cells.append('rect')
		.attr({
			'x': function(d) { return corXscale(d.col); },
			'y': function(d) { return corYscale(d.row); },
			'width': corXscale.rangeBand(),
			'height': corYscale.rangeBand(),
			'fill': 'none',
			'stroke': 'none',
			'stroke-width': '1'
		});

	var circles = cells.append('circle')
		.attr('cx', function(d) {return corXscale(d.col) + 0.5*corXscale.rangeBand(); })
		.attr('cy', function(d) {return corYscale(d.row) + 0.5*corYscale.rangeBand(); })
		.attr('r', function(d) {return corRscale(Math.abs(d.value)); })
		.style('fill', function(d) { return corColScale(d.value); });

	corrplot.selectAll('g.cell')
	.on('mouseover', function(d) {
		console.log()
		d3.select(this)
		.select('rect')
		.attr('stroke', 'black');

		var xPos = parseFloat(d3.select(this).select('rect').attr('x'));
		var yPos = parseFloat(d3.select(this).select('rect').attr('y'));

		corrplot.append('text')
		.attr({
			'class': 'corrlabel',
			'x': corXscale(d.col) + 0.5*corXscale.rangeBand(),
			'y': h - h_smaller + labelsize
		})
		.text((is_X_Y ? vars_Y : vars)[d.col])
		.attr({
			'dominant-baseline': 'middle',
			'text-anchor': 'middle'
		})
		.style("font-size", labelsize+"px");

		corrplot.append('text')
		.attr({
			'class': 'corrlabel'
			// 'x': -margin.left*0.1,
			// 'y': corXscale(d.row)
		})
		.text((is_X_Y ? vars_X : vars)[d.row])
		.attr({
			'dominant-baseline': 'middle',
			'text-anchor': 'middle',
			'transform': 'translate(' + (-labelsize) + ',' + (corYscale(d.row) + 0.5*corYscale.rangeBand()) + ')rotate(270)'
		})
		.style("font-size", labelsize+"px");

		corrplot.append('rect')
		.attr({
			'class': 'tooltip',
			'x': xPos - 20 + corXscale.rangeBand() / 2,
			'y': yPos - 30,
			'width': 40,
			'height': 20,
			'fill': 'rgba(200, 200, 200, 0.5)',
			'stroke': 'black'
		});

		corrplot.append('text')
		.attr({
			'class': 'tooltip',
			'x': xPos + corXscale.rangeBand() / 2,
			'y': yPos - 15,
			'text-anchor': 'middle',
			'font-family': 'sans-serif',
			'font-size': '14px',
			'font-weight': 'bold',
			'fill': 'black'
		})
		.text(d3.format('.2f')(d.value));
	}) // function for mouseover
		.on('mouseout', function(d) {
			d3.select('#corrtext').remove();
		d3.selectAll('.corrlabel').remove();
		d3.select(this)
			.select('rect')
			.attr('stroke', 'none');
		//Hide the tooltip
		d3.selectAll('.tooltip').remove();
	})
	.on('click', function(d) {
		d3.selectAll('.scatplottitle').remove();
		drawScatter(d.col, d.row, whichrawdat);
	});
} // Definition of drawD3