function getPlaylist() {
  $.ajax({
  	url : "http://s5.radioboss.fm:8380/played.html?sid=1&type=json",
    // url: "http://localhost:5000/played.json",
  	dataType: "JSONP",
  	type : "GET",

  	success: function(data){
      const currentTrack = data[0]['title'];
      $("#current-track").html(currentTrack);

      let lastTracks = [];
      for (let i = 0; i <= 9; i++) {
        lastTracks += '<li>'+data[i]['title']+'</li>'
      };
      $("#last-tracks").html(lastTracks);
  	}
  });
};
setInterval(getPlaylist, 7500);
