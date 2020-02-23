var is_X_Y = (typeof vars_X !== 'undefined');

for (var varname in window){
	if (varname.includes("_") && (varname.substring(0,3) == 'cor' || varname.substring(0,4) == 'diff')){
		window[varname + "_mat"] = [];
		for (var i = 0; i < window[varname].length; ++i) {
			for (var j = 0; j < window[varname][i].length; ++j) {
				window[varname+"_mat"].push({row: j, col: i, value:window[varname][i][j]}); // json written by column in R; so need to reverse when reading in
			}
		}
		window[varname] = null;
	}
}

if (is_X_Y) {
	var nind_first = dat_first_X.ind.length,
		nind_second = dat_second_X.ind.length,
		nvar_X = vars_X.length,
		nvar_Y = vars_Y.length
} else {
	var nind_first = dat_first.ind.length,
		nind_second = dat_second.ind.length,
		nvar_X = vars.length,
		nvar_Y = vars.length
}

var w = 650, // ideal width for correlation plot; may be changed for the corr plot if number of row variables smaller than number of column variables
	h = 650, // common height for correlation plot (from right below title to end of bounding box) and scatter plots (from right below title for the 1st scatter plot to right above the variable name at the bottom); may be changed for the corr plot if number of column variables smaller than number of row variables
	w_scat = w / 2;

var labelsize = w / 30; // Size of texts (titles, variable names)

var margin = {top: labelsize*2, right: labelsize*2, bottom: labelsize*2, left: labelsize*2};

if (nvar_Y > nvar_X) { // more variables to plot on the x axis, make h smaller and fill the margin
	h_smaller = h - h / nvar_Y * nvar_X;
	w_smaller = 0;
} else {
	w_smaller = w - w / nvar_X * nvar_Y;
	h_smaller = 0;
}

var pad = 2 * labelsize + 30;
var full_width = w + pad + w_scat;
var h_btw_scat = 2*labelsize + 20; // Distance between two scatter plots (in case of two-sample)
var num_ticks = 8; // Number of ticks in the axes for the scatterplot(s)

document.getElementById("d3orcytoscape").style.left = margin.left+"px";
document.getElementById("oneortwo").style.left = margin.left+"px";
document.getElementById("cortype").style.left = margin.left+"px";
var right_side_buttons_left = margin.left + full_width - Math.max(document.getElementById("whichdataid").getBoundingClientRect().width, document.getElementById("testtype").getBoundingClientRect().width, document.getElementById("whichlayout").getBoundingClientRect().width);
document.getElementById("whichlayout").style.left = right_side_buttons_left + "px";
document.getElementById("whichdataid").style.left = right_side_buttons_left + "px";
document.getElementById("testtype").style.left = right_side_buttons_left + "px";
document.getElementById("whichdatalabelFIRST").innerHTML = first_name
document.getElementById("whichdatalabelSECOND").innerHTML = second_name


var cyto_cor_text_size = Math.min(labelsize, 15);
var cyto_prompt = "Please left click on/drag a node or left click on an edge on the left.</br></br>You may also zoom in/out the canvas.</br></br>Right click, or left click on the white spaces to the left/right of the graph to reset.";
document.getElementById("cor_list").style["font-size"] = labelsize + "px";
document.getElementById("cor_list").innerHTML = cyto_prompt;


