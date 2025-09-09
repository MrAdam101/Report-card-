const positiveComments = [
  "shows great enthusiasm for learning and participates actively in class discussions.",
  "is making steady progress in developing English communication skills.",
  "displays creativity and curiosity in classroom activities.",
  "works well with peers and demonstrates good teamwork.",
  "is becoming more confident in using English in daily routines.",
  "shows excellent listening skills and responds well to instructions.",
  "is developing a positive attitude towards learning English."
];

const improvementComments = [
  "could focus on improving pronunciation for clearer communication.",
  "should continue practicing reading to build stronger fluency.",
  "can work on expanding vocabulary to express ideas more effectively.",
  "would benefit from more practice in writing full sentences.",
  "should try to participate more actively in group discussions.",
  "can continue to develop confidence when speaking in front of the class."
];

document.getElementById('reportForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const name = document.getElementById('name').value;
  const className = document.getElementById('class').value;
  const gender = document.getElementById('gender').value;
  const age = document.getElementById('age').value;

  const positive = positiveComments[Math.floor(Math.random() * positiveComments.length)];
  const improvement = improvementComments[Math.floor(Math.random() * improvementComments.length)];

  const pronoun = gender === 'boy' ? 'He' : 'She';

  const report = `
    <h2>Report for ${name}</h2>
    <p><strong>Class:</strong> ${className}</p>
    <p><strong>Age:</strong> ${age}</p>
    <p>${name} ${positive} ${pronoun} ${improvement}</p>
  `;

  const reportDiv = document.getElementById('reportOutput');
  reportDiv.style.display = 'block';
  reportDiv.innerHTML = report;
});
