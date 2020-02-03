document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('#inputForm').onsubmit = () => {
    // Hide results from previous request

    // create request. 
    const request = new XMLHttpRequest();
    const text = document.querySelector('#inputText').value;
    request.open('Post', '/vader/predict')

    // callback function for when the request completes. 
    request.onload = function() {

        // collect data from request
        const data = JSON.parse(request.responseText);
        const compound =  data.compound
        const positive =  data.pos
        const neutral = data.neu
        const negative = data.neg
        var descriptor = ''
        var sentiment = ''

        // organize data from response
        if (compound < -0.25) {
            descriptor = 'Leans'
            sentiment = 'Negative'
            if (compound < -0.50) {
                descriptor = 'Likely'
            } 
          } else if (compound > 0.25) {
            descriptor = 'Leans'
            sentiment = 'Positive'
            if (compound > 0.50) {
                descriptor = 'Likely'
            } 
          } else {
            sentiment = 'Neutral'
          }
        
        const cmd_contents = `${descriptor} ${sentiment} - Compound Score:${compound}`;
        const pos_contents = `Score: ${positive}`;
        const neu_contents = `Score: ${neutral}`;
        const neg_contents = `Score: ${negative}`;

        // Update UI items with results
        document.querySelector('#compound').innerHTML = cmd_contents;
        document.querySelector('#positive').innerHTML = pos_contents;
        document.querySelector('#neutral').innerHTML = neu_contents;
        document.querySelector('#negative').innerHTML = neg_contents;

        // Make results visible
        document.querySelector('#compound').hidden = false;
        document.querySelector('#positive').hidden = false;
        document.querySelector('#neutral').hidden = false;
        document.querySelector('#negative').hidden = false;

        
    
    }
    // add data to sent with request
    const data = new FormData();
    data.append('text', text);

    // send request
    request.send(data);
    return false;};
});
