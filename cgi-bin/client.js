let emojiButtonToggle = false;
let timer = null;

$('.emoji-nav .emoji').click(function(){
  $('.emoji-menu-button').html($(this).html());
  const navButtons = $('.emoji-nav .emoji').toArray();
  const emojiMenus = $(".emoji-menu [id*='menu']").toArray();
    $('.emoji-nav .emoji').removeClass('active');

  let newButton = $(this).attr('id').split('-')[0];

  for(let i in emojiMenus) {
    let newMenu = emojiMenus[i].id.split('-')[0];
    if(newMenu == newButton) {
      $('#' + newMenu + '-menu').show();
    } else {
      $('#' + newMenu + '-menu').hide();
    }
  }
  $(this).addClass('active');
});

$('.emoji-menu-button').click(function() {
  emojiButtonToggle = !emojiButtonToggle;
    if(emojiButtonToggle) {
        $('.emoji-dialog').addClass('move-up');
    } else {
        $('.emoji-dialog').removeClass('move-up');
    }
});

$('.emoji-menu-button').hover(function() {
  $('.emoji-menu-button').html("😄");
});

$('.emoji-menu-button').mouseout(function() {
  $('.emoji-menu-button').html("🙂");
});

$('.emoji-menu-button').mousedown(function() {
  $('.emoji-menu-button').html("😉");
});

$('#emoji-search').keyup(function() {
  clearTimeout(timer);
  timer = setTimeout(searchEmojis, 300)
});

function searchEmojis() {
  $('#activities-menu').empty();
  const searchValue = $('#emoji-search').val().toLowerCase().trim();
  for(let i in activities.activity) {
    let emojiKey = activities.activity[i].key.split('_').join(' ').trim();
    // console.log(emojiKey + ": " + searchValue);
   // console.log("Emoji index: " + emojiKey.indexOf(searchValue));
    // console.log("Word length: " + searchValue.length);
    if(emojiKey.includes(searchValue) > 0) {
        $('.emoji-menu #activities-menu').append($('<div class="emoji">').text(activities.activity[i].value));
  $('.emoji-menu .emoji').click(function(){
  $('.emoji-menu-button').html($(this).html());
  });
       }
    // console.log(activities.activity[i].value);
  }

  if (searchValue.length == 0){
         $('#activities-menu').empty();
          for(let i in activities.activity) {
  $('.emoji-menu #activities-menu').append($('<div class="emoji">').text(activities.activity[i].value));
  $('.emoji-menu .emoji').click(function(){
  $('.emoji-menu-button').html($(this).html());
});
       }
  }
}
  const activities =  {
    "activity": [
      {
        "key": "soccer_ball",
        "value": "⚽"
      },
      {
        "key": "basket_ball",
        "value": "🏀"
      },
      {
        "key": "american_football",
        "value": "🏈"
      },
      {
        "key": "baseball",
        "value": "⚾"
      },
      {
        "key": "tennis_racquet_ball",
        "value": "🎾"
      },
      {
        "key": "volley_ball",
        "value": "🏐"
      },
      {
        "key": "rugby_football",
        "value": "🏉"
      },
      {
        "key": "billiards",
        "value": "🎱"
      },
      {
        "key": "activity_in_hole",
        "value": "⛳"
      },
      {
        "key": "golfer",
        "value": "🏌"
      },
      {
        "key": "table_tennis_paddle_ball",
        "value": "🏓"
      },
      {
        "key": "badminton_racquet_shuttle_cock",
        "value": "🏸"
      },
      {
        "key": "ice_hockey_stick_puck",
        "value": "🏒"
      },
      {
        "key": "field_hockey_stick_ball",
        "value": "🏑"
      },
      {
        "key": "cricket_bat_ball",
        "value": "🏏"
      },
      {
        "key": "ski_and_ski_boot",
        "value": "🎿"
      },
      {
        "key": "skier",
        "value": "⛷"
      },
      {
        "key": "snow_boarder",
        "value": "🏂"
      },
      {
        "key": "ice_skate",
        "value": "⛸"
      },
      {
        "key": "bow_and_arrow",
        "value": "🏹"
      },
      {
        "key": "fishing_pole_and_fish",
        "value": "🎣"
      },
      {
        "key": "row_boat",
        "value": "🚣"
      },
      {
        "key": "row_boat_type_1_2",
        "value": "🚣🏻"
      },
      {
        "key": "row_boat_type_3",
        "value": "🚣🏼"
      },
      {
        "key": "row_boat_type_4",
        "value": "🚣🏽"
      },
      {
        "key": "row_boat_type_5",
        "value": "🚣🏾"
      },
      {
        "key": "row_boat_type_6",
        "value": "🚣🏿"
      },
      {
        "key": "swimmer",
        "value": "🏊"
      },
      {
        "key": "swimmer_type_1_2",
        "value": "🏊🏻"
      },
      {
        "key": "swimmer_type_3",
        "value": "🏊🏼"
      },
      {
        "key": "swimmer_type_4",
        "value": "🏊🏽"
      },
      {
        "key": "swimmer_type_5",
        "value": "🏊🏾"
      },
      {
        "key": "swimmer_type_6",
        "value": "🏊🏿"
      },
      {
        "key": "surfer",
        "value": "🏄"
      },
      {
        "key": "surfer_type_1_2",
        "value": "🏄🏻"
      },
      {
        "key": "surfer_type_3",
        "value": "🏄🏼"
      },
      {
        "key": "surfer_type_4",
        "value": "🏄🏽"
      },
      {
        "key": "surfer_type_5",
        "value": "🏄🏾"
      },
      {
        "key": "surfer_type_6",
        "value": "🏄🏿"
      },
      {
        "key": "bath",
        "value": "🛀"
      },
      {
        "key": "bath_type_1_2",
        "value": "🛀🏻"
      },
      {
        "key": "bath_type_3",
        "value": "🛀🏼"
      },
      {
        "key": "bath_type_4",
        "value": "🛀🏽"
      },
      {
        "key": "bath_type_5",
        "value": "🛀🏾"
      },
      {
        "key": "bath_type_6",
        "value": "🛀🏿"
      },
      {
        "key": "person_with_ball",
        "value": "⛹"
      },
      {
        "key": "person_with_ball_type_1_2",
        "value": "⛹🏻"
      },
      {
        "key": "person_with_ball_type_3",
        "value": "⛹🏼"
      },
      {
        "key": "person_with_ball_type_4",
        "value": "⛹🏽"
      },
      {
        "key": "person_with_ball_type_5",
        "value": "⛹🏾"
      },
      {
        "key": "person_with_ball_type_6",
        "value": "⛹🏿"
      },
      {
        "key": "weight_lifter",
        "value": "🏋"
      },
      {
        "key": "weight_lifter_type_1_2",
        "value": "🏋🏻"
      },
      {
        "key": "weight_lifter_type_3",
        "value": "🏋🏼"
      },
      {
        "key": "weight_lifter_type_4",
        "value": "🏋🏽"
      },
      {
        "key": "weight_lifter_type_5",
        "value": "🏋🏾"
      },
      {
        "key": "weight_lifter_type_6",
        "value": "🏋🏿"
      },
      {
        "key": "bicyclist",
        "value": "🚴"
      },
      {
        "key": "bicyclist_type_1_2",
        "value": "🚴🏻"
      },
      {
        "key": "bicyclist_type_3",
        "value": "🚴🏼"
      },
      {
        "key": "bicyclist_type_4",
        "value": "🚴🏽"
      },
      {
        "key": "bicyclist_type_5",
        "value": "🚴🏾"
      },
      {
        "key": "bicyclist_type_6",
        "value": "🚴🏿"
      },
      {
        "key": "mountain_bicyclist",
        "value": "🚵"
      },
      {
        "key": "mountain_bicyclist_type_1_2",
        "value": "🚵🏻"
      },
      {
        "key": "mountain_bicyclist_type_3",
        "value": "🚵🏼"
      },
      {
        "key": "mountain_bicyclist_type_4",
        "value": "🚵🏽"
      },
      {
        "key": "mountain_bicyclist_type_5",
        "value": "🚵🏾"
      },
      {
        "key": "mountain_bicyclist_type_6",
        "value": "🚵🏿"
      },
      {
        "key": "horse_racing",
        "value": "🏇"
      },
      {
        "key": "horse_racing_type_1_2",
        "value": "🏇🏻"
      },
      {
        "key": "horse_racing_type_3",
        "value": "🏇🏻"
      },
      {
        "key": "horse_racing_type_4",
        "value": "🏇🏽"
      },
      {
        "key": "horse_racing_type_5",
        "value": "🏇🏾"
      },
      {
        "key": "horse_racing_type_6",
        "value": "🏇🏿"
      },
      {
        "key": "main_business_suit_levitating",
        "value": "🕴"
      },
      {
        "key": "trophy",
        "value": "🏆"
      },
      {
        "key": "running_shirt_with_sash",
        "value": "🎽"
      },
      {
        "key": "sports_medal",
        "value": "🏅"
      },
      {
        "key": "military_medal",
        "value": "🎖"
      },
      {
        "key": "reminder_ribbon",
        "value": "🎗"
      },
      {
        "key": "rosette",
        "value": "🏵"
      },
      {
        "key": "ticket",
        "value": "🎫"
      },
      {
        "key": "admission_tickets",
        "value": "🎟"
      },
      {
        "key": "performing_arts",
        "value": "🎭"
      },
      {
        "key": "artist_palette",
        "value": "🎨"
      },
      {
        "key": "circus_tent",
        "value": "🎪"
      },
      {
        "key": "microphone",
        "value": "🎤"
      },
      {
        "key": "headphone",
        "value": "🎧"
      },
      {
        "key": "musical_score",
        "value": "🎼"
      },
      {
        "key": "musical_keyboard",
        "value": "🎹"
      },
      {
        "key": "saxophone",
        "value": "🎷"
      },
      {
        "key": "trumpet",
        "value": "🎺"
      },
      {
        "key": "guitar",
        "value": "🎸"
      },
      {
        "key": "violin",
        "value": "🎻"
      },
      {
        "key": "clapper_board",
        "value": "🎬"
      },
      {
        "key": "video_game",
        "value": "🎮"
      },
      {
        "key": "alien_monster",
        "value": "👾"
      },
      {
        "key": "direct_hit",
        "value": "🎯"
      },
      {
        "key": "game_die",
        "value": "🎲"
      },
      {
        "key": "slot_machine",
        "value": "🎰"
      },
      {
        "key": "bowling",
        "value": "🎳"
      },
    ]
  }
for(let i in activities.activity) {
  $('.emoji-menu #activities-menu').append($('<div class="emoji">').text(activities.activity[i].value));
  $('.emoji-menu .emoji').click(function(){
  $('.emoji-menu-button').html($(this).html());
});
}