$(document).ready(function () {
    
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'bounceIn',
        },
        out:{
            effect: 'bounceOut',
        },
    });
    // Siri configuration
     var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: "ios9",
    amplitude: "1",
    speed: "0.30",
    autostart: true,
  });

  // Siri message animation
  $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'fadeInUp',
            sync: true,
        },
        out:{
            effect: 'fadeOutUp',
            sync: true,
        },
    });

    // Mic button click event
    $('#MicBtn').click(function () { 
        eel.playAssistantSound();
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.takecommand(); // Fixed: removed extra ()
    });
});

// Expose DisplayMessage to eel so Python can call it
// You can update this to show the message in your UI instead of alert

eel.expose(DisplayMessage);
function DisplayMessage(msg) {
    alert(msg); // Replace with custom UI update if needed
}
