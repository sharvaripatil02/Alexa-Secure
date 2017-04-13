
// Twilio Credentials 
var accountSid = 'AC991474631891e4378477a777540a95ce';
var authToken = '90f19b1637d3262c7a0683624686443b';
var fromNumber = '+16315930820';
//var to='+13124682137';
var https = require('https');
var queryString = require('querystring');

// Lambda function:
exports.handler = function (event, context) {

    console.log('Running event');
    
    // Send an SMS message to the number provided in the event data.
    // End the lambda function when the send function completes.
    SendSMS(event.to, 'Hello from Lambda Functions!', 
                function (status) { context.done(null, status); });  
};

// Sends an SMS message using the Twilio API
// to: Phone number to send to
// body: Message body
// completedCallback(status) : Callback with status message when the function completes.
function SendSMS(to, body) {
    
    // The SMS message to send
    var message = {
        To:'+13124682137', 
        From: fromNumber,
        Body: body
    };
    
    var messageString = queryString.stringify(message);
    
    // Options and headers for the HTTP request   
    var options = {
        host: 'api.twilio.com',
        port: 443,
        path: '/2010-04-01/Accounts/' + accountSid + '/Messages.json',
        method: 'POST',
        headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Content-Length': Buffer.byteLength(messageString),
                    'Authorization': 'Basic ' + new Buffer(accountSid + ':' + authToken).toString('base64')
                 }
    };
    
    // Setup the HTTP request
    var req = https.request(options, function (res) {

        res.setEncoding('utf-8');
              
        // Collect response data as it comes back.
        var responseString = '';
        res.on('data', function (data) {
            responseString += data;
        });
        
        // Log the responce received from Twilio.
        // Or could use JSON.parse(responseString) here to get at individual properties.
        res.on('end', function () {
            console.log('Twilio Response: ' + responseString);
            
            var parsedResponse = JSON.parse(responseString);
            
            var sessionAttributes = {};
            var cardTitle = "Sent";
            var speechOutput = "Ok, Sms sent.";
            
            var repromptText = "";
            var shouldEndSession = true;
            
            if("queued" === parsedResponse.status){  // we're good, variables already set..
            } else {
                speechOutput = parsedResponse.message;
            }
            

            callback(sessionAttributes,
                     buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession));
            
            
        });
    });
    
    // Handler for HTTP request errors.
    req.on('error', function (e) {
        console.error('HTTP error: ' + e.message);
        
        var sessionAttributes = {};
            var cardTitle = "Sent";
            var speechOutput = "Unfortunately, sms request has finished with errors.";
            
            var repromptText = "";
            var shouldEndSession = true;

            callback(sessionAttributes,
                     buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession));
        
    });
    
    // Send the HTTP request to the Twilio API.
    // Log the message we are sending to Twilio.
    console.log('Twilio API call: ' + messageString);
    req.write(messageString);
    req.end();

}

// Route the incoming request based on type (LaunchRequest, IntentRequest,
// etc.) The JSON body of the request is provided in the event parameter.
exports.handler = function (event, context) {
    try {
        console.log("event.session.application.applicationId=" + event.session.application.applicationId);

        /**
         * Uncomment this if statement and populate with your skill's application ID to
         * prevent someone else from configuring a skill that sends requests to this function.
         */
        /*
        if (event.session.application.applicationId !== "amzn1.echo-sdk-ams.app.[unique-value-here]") {
             context.fail("Invalid Application ID");
         }
        */

        if (event.session.new) {
            onSessionStarted({requestId: event.request.requestId}, event.session);
        }

        if (event.request.type === "LaunchRequest") {
            onLaunch(event.request,
                     event.session,
                     function callback(sessionAttributes, speechletResponse) {
                        context.succeed(buildResponse(sessionAttributes, speechletResponse));
                     });
        }  else if (event.request.type === "IntentRequest") {
            onIntent(event.request,
                     event.session,
                     function callback(sessionAttributes, speechletResponse) {
                         context.succeed(buildResponse(sessionAttributes, speechletResponse));
                     });
        } else if (event.request.type === "SessionEndedRequest") {
            onSessionEnded(event.request, event.session);
            context.succeed();
        }
    } catch (e) {
        context.fail("Exception: " + e);
    }
};

/**
 * Called when the session starts.
 */
function onSessionStarted(sessionStartedRequest, session) {
    console.log("onSessionStarted requestId=" + sessionStartedRequest.requestId +
            ", sessionId=" + session.sessionId);
}

/**
 * Called when the user launches the skill without specifying what they want.
 */
function onLaunch(launchRequest, session, callback) {
   // console.log("onLaunch requestId=" + launchRequest.requestId +
   //         ", sessionId=" + session.sessionId);

    // Dispatch to your skill's launch.
    getWelcomeResponse(callback);
}

exports.handler = function(event, context) {
console.log('Loading function');
var aws = require('aws-sdk');
var s3 = new aws.S3({apiVersion: '2006-03-01'});
console.log('Received event:', JSON.stringify(event, null, 2));
console.log("Req =", event.Records[0].s3.bucket.name);
//console.log('Event source', event.source);
//  "eventSource": "aws:s3"
    // Get the object from the event and show its content type
//var bucket = "mhacks0228";
//var key = "3niq6VMTlmSB3EhiiwtntriKNuUhB62buy9xNz0I";
 //   s3.getObject({Bucket: bucket, Key: key}, function(err, data) {
  //      if (err) {
 // this.awsBucketName
 // new aws.S3().getObject({ Bucket: "mhacks0228" , Key: "3niq6VMTlmSB3EhiiwtntriKNuUhB62buy9xNz0I"  }, function(err, data)
//{
  //  if (!err)
  
    //{    console.log(data.Body.toString());
        //    console.log("Error getting object " + key + " from bucket " + bucket +
       //         ". Make sure they exist and your bucket is in the same region as this function.");
     //       context.fail ("Error getting file: " + err)      
    //    } 
     //   else
    //    {
    if(event.Records[0].s3.bucket.name === "sourcebucket")
    {
             console.log("received SendSms intent.");
       // console.log("slots: "+intentRequest.intent.slots);
        var destination = 'wife';
        var text = 'New code';
        console.log("Sending sms to : "+ destination+" with text: "+text);
        
        var number;
        if("wife" === destination)
        {
            number = "+13124682137";
        } 
        else if ("husband" === destination)
        {
            number = "+13129459631";
        }
    // else {
     //   throw "Invalid intent";
//    }
            SendSMS(number ,text);
        // getWelcomeResponse(callback);
          var sessionAttributes = {};
            var cardTitle = "Sent";
            var speechOutput = "Suspicious activity. Sms sent.";
            
            var repromptText = "";
            var shouldEndSession = true;

                     buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession);
           
    
           // console.log('CONTENT TYPE:', data.ContentType);
            context.succeed();
    }
 //      }
     else
      {
           console.log("Error" + err);
           //console.log(aws.)
     }
//    });
};

/**
 * Called when the user specifies an intent for this skill.
 */
function onIntent(intentRequest, session, callback) {
    console.log("onIntent requestId=" + intentRequest.requestId +
            ", sessionId=" + session.sessionId);

    var intent = intentRequest.intent,
        intentName = intentRequest.intent.name;

    
    if("SendSms" === intentName){
        console.log("received SendSms intent.");
        console.log("slots: "+intentRequest.intent.slots);
        var destination = intentRequest.intent.slots.Destination.value;
        var text = intentRequest.intent.slots.Text.value;
        console.log("Sending sms to : "+ destination+" with text: "+text);
        
        var number;
        if("wife" === destination){
            number = "+13124682137";
        } else if ("husband" === destination){
            number = "+13129459631";
        }
        SendSMS(number ,text);
    } else {
        throw "Invalid intent";
    }
}

/**
 * Called when the user ends the session.
 * Is not called when the skill returns shouldEndSession=true.
 */
function onSessionEnded(sessionEndedRequest, session) {
    console.log("onSessionEnded requestId=" + sessionEndedRequest.requestId +
            ", sessionId=" + session.sessionId);
    // Add cleanup logic here
}

// --------------- Functions that control the skill's behavior -----------------------



function getWelcomeResponse(callback) {
    // If we wanted to initialize the session to have some attributes we could add those here.
    var sessionAttributes = {};
    var cardTitle = "Welcome";
    var speechOutput = "Suspicious entry. Sms sent.";
    // If the user either does not reply to the welcome message or says something that is not
    // understood, they will be prompted again with this text.
    //var repromptText = "Please tell me what action to undertake. ";
    var shouldEndSession = false;

    callback(sessionAttributes,
             buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession));
}
// --------------- Helpers that build all of the responses -----------------------

function buildSpeechletResponse(title, output, repromptText, shouldEndSession) {
    return {
        outputSpeech: {
            type: "PlainText",
            text: output
        },
        card: {
            type: "Simple",
            title: "SessionSpeechlet - " + title,
            content: "SessionSpeechlet - " + output
        },
        reprompt: {
            outputSpeech: {
                type: "PlainText",
                text: repromptText
            }
        },
        shouldEndSession: shouldEndSession
    };
}

function buildResponse(sessionAttributes, speechletResponse) {
    return {
        version: "1.0",
        sessionAttributes: sessionAttributes,
        response: speechletResponse
    };
}
