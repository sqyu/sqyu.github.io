var cortype = "spearman", testtype = "perm", two = 1, d3ORctyo=0, whichdata = "first", whichlayout="grid",
	dataradios = document.getElementById('whichdataid'),
	testcairadio = document.getElementById('testtypecai'),
	testcaitext = document.getElementById('testtypecaitext'),
	testrawradio = document.getElementById('testtyperaw'),
	testrawtext = document.getElementById('testtyperawtext'),
	layoutradios = document.getElementById('whichlayout');
autohideradios();

//switch_div(d3ORctyo);
Draw();

d3.selectAll("input[name='d3orcytoscape']").on("change", function () {
	d3ORctyo = +this.value;
	autohideradios();
	if (d3ORctyo && testtype === "raw")
		toperm("raw");
	toggle_div()//switch_div(d3ORctyo);
	Draw();
})
d3.selectAll("input[name='whichlayout']").on("change", function () {
	whichlayout = this.value;
	Draw();
})
d3.selectAll("input[name='oneortwo']").on("change", function () {
	two = +this.value;
	prefix = +two ? "diff" : "cor";
	autohideradios();
	if (!two) {
		whichdata = getradiovalue(dataradios);
		if (testtype === "cai") 
			toperm("cai");
	}
	Draw();
})
d3.selectAll("input[name='whichdata']").on("change", function () {
	whichdata = this.value;
	Draw();
})
d3.selectAll("input[name='cortype']").on("change", function () {
	cortype = this.value;
	autohideradios();
	if (cortype !== "pearson" && testtype === "cai")
		toperm("cai");
	Draw();
})
d3.selectAll("input[name='testtype']").on("change", function () {
	testtype = this.value;
	Draw();
})
