function populateScoreInContainer(score, $container) {
    var margin = Math.floor(Math.random() * 600) + 200;
    var html = '<div class="score" style="margin-top:' + margin + 'px;">';

    html += '<h1 class="score-title">' + score.title + '</h1>';
    for (var i=0; i<score.description.length; i++) {
        html += '<p class="score-description">' + score.description[i] + '</p>';
    }

    html += '</div>';

    $container.append(html);
}
var scores = scores;
var scoreCount = scores.length;
var index;
var $columns = $('.column');
var columnIndex = 0;

for (var i=0; i<scoreCount; i++) {
    index = Math.floor(Math.random() * scoreCount);
    populateScoreInContainer(scores[index], $columns.eq(columnIndex));
    columnIndex = (columnIndex < 3) ? columnIndex + 1 : 0;
}