let sections = document.getElementsByTagName('section');

assert.equal(sections[0].style.display, '', 'First section has invalid display');
assert.equal(sections[1].style.display, '', 'Second section has invalid display');
assert.equal(sections[2].style.display, '', 'Third section has invalid display');

sections[0].querySelectorAll('.answer-text')[0].click();

assert.equal(sections[0].style.display, 'none', 'First section has invalid display');
assert.equal(sections[1].style.display, 'block', 'Second section has invalid display');
assert.equal(sections[2].style.display, '', 'Third section has invalid display');