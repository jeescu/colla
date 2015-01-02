var activity = document.getElementById('tab-activity');
var project = document.getElementById('tab-project');
var monitor = document.getElementById('tab-monitor');
var graph = document.getElementById('tab-graph');
var issue = document.getElementById('tab-issue');

function actShow() {
    document.getElementById('fragment-activity').classList.remove('hidden');
    document.getElementById('fragment-project').classList.add('hidden');
    document.getElementById('fragment-monitor').classList.add('hidden');
    document.getElementById('fragment-graph').classList.add('hidden');
    document.getElementById('fragment-issue').classList.add('hidden');
}

function proShow() {
    document.getElementById('fragment-project').classList.remove('hidden');
    document.getElementById('fragment-activity').classList.add('hidden');
    document.getElementById('fragment-monitor').classList.add('hidden');
    document.getElementById('fragment-graph').classList.add('hidden');
    document.getElementById('fragment-issue').classList.add('hidden');
}

function monShow() {
    document.getElementById('fragment-monitor').classList.remove('hidden');
    document.getElementById('fragment-project').classList.add('hidden');
    document.getElementById('fragment-activity').classList.add('hidden');
    document.getElementById('fragment-graph').classList.add('hidden');
    document.getElementById('fragment-issue').classList.add('hidden');
}

function graphShow() {
    document.getElementById('fragment-graph').classList.remove('hidden');
    document.getElementById('fragment-project').classList.add('hidden');
    document.getElementById('fragment-monitor').classList.add('hidden');
    document.getElementById('fragment-activity').classList.add('hidden');
    document.getElementById('fragment-issue').classList.add('hidden');
}

function issueShow() {
    document.getElementById('fragment-issue').classList.remove('hidden');
    document.getElementById('fragment-project').classList.add('hidden');
    document.getElementById('fragment-monitor').classList.add('hidden');
    document.getElementById('fragment-graph').classList.add('hidden');
    document.getElementById('fragment-activity').classList.add('hidden');
}

function init() {
	activity.addEventListener("click", actShow);
    project.addEventListener("click", proShow);
    monitor.addEventListener("click", monShow);
    graph.addEventListener("click", graphShow);
    issue.addEventListener("click", issueShow);
}

window.addEventListener("load", init);