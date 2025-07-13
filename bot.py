<?php
/*
13HACK-@SossherTV2
*/
ob_start();
define('API_KEY','7530531822:AAHPGBMzrBYcZ3krh0ujC8yVJSFCohfTQIY');
//-----------------------------------------------------------------------------------------
//فانکشن sizdahorg :
function sizdahorg($method,$datas=[]){
    $url = "https://api.telegram.org/bot".API_KEY."/".$method;
    $ch = curl_init();
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
    $res = curl_exec($ch);
    if(curl_error($ch)){
        var_dump(curl_error($ch));
    }else{
        return json_decode($res);
    }
}
//-----------------------------------------------------------------------------------------
//متغیر ها :
// msg
$Dev = array("7530531822","7530531822","7530531822"); 
@$usernamebot = "Funfunichat_bot"; 
@$channel = "SossherTV2"; 
$token = API_KEY;
$web = "00000000000"; 
//-----------------------------------------------------------------------------------------------
$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$from_id = $message->from->id;
$chat_id = $message->chat->id;
$message_id = $message->message_id;
$first_name = $message->from->first_name;
$last_name = $message->from->last_name;
$username = $message->from->username;
$textmassage = $message->text;
$firstname = $update->callback_query->from->first_name;
$usernames = $update->callback_query->from->username;
$chatid = $update->callback_query->message->chat->id;
$fromid = $update->callback_query->from->id;
$membercall = $update->callback_query->id;
//------------------------------------------------------------------------
$forward_from_chat = $update->message->forward_from_chat;
$from_chat_id = $forward_from_chat->id;
$data = $update->callback_query->data;
$messageid = $update->callback_query->message->message_id;
$tc = $update->message->chat->type;
$forward_from = $update->message->forward_from;
$forward_from_id = $forward_from->id;
$forward_from_username = $forward_from->username;
$reply = $update->message->reply_to_message->forward_from->id;
@$caption = $update->message->caption;
@$rt = $update->message->reply_to_message;
// ========================================================================
$forchannel = json_decode(file_get_contents("https://api.telegram.org/bot".$token."/getChatMember?chat_id=@".$channel."&user_id=".$from_id));
$tch = $forchannel->result->status;
$forchannelq = json_decode(file_get_contents("https://api.telegram.org/bot".$token."/getChatMember?chat_id=@".$channel."&user_id=".$fromid));
$tchq = $forchannelq->result->status;
//-----------------------------------------------------------------------------------------
@$user = json_decode(file_get_contents("data/user.json"),true);
//=================================================================================================
//فانکشن ها :
function SendMessage($chat_id, $text){
sizdahorg('sendMessage',[
'chat_id'=>$chat_id,
'text'=>$text,
'parse_mode'=>'MarkDown']);
}
 function Forward($berekoja,$azchejaei,$kodompayam)
{
sizdahorg('ForwardMessage',[
'chat_id'=>$berekoja,
'from_chat_id'=>$azchejaei,
'message_id'=>$kodompayam
]);
}
function  getUserProfilePhotos($token,$from_id) {
  $url = 'https://api.telegram.org/bot'.$token.'/getUserProfilePhotos?user_id='.$from_id;
  $result = file_get_contents($url);
  $result = json_decode ($result);
  $result = $result->result;
  return $result;
}
//======================================================================
if(!in_array($from_id, $user["userlist"])) {
$user["userlist"][]="$from_id";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
    }
//==================================================================
if(in_array($from_id, $user["blocklist"])) {
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🛑شما به خاطر رعایت نکردن قوانین از ربات مسدود شدید 

❇️ لطفا پیام دوباره ارسال نکنید",
'reply_markup'=>json_encode(['KeyboardRemove'=>[
],'remove_keyboard'=>true
])
    		]);
}
if($textmassage=="/start" && $tc == "private"){	
if(in_array($from_id, $user["userlist"]) == true) {
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"به منوی اصلی ربات خوش امدید🎉

🔻 از دکمه های زیر استفاده کنید 🔻",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
			[
				['text'=>"💬 چت ناشناس"]
				],
								[
				['text'=>"🏅 حساب ویژه"],['text'=>"💎 اطلاعات حساب|ویرایش"]
				],
												[
				['text'=>"👫 لیست دوستان"],['text'=>"🚫 لیست بلاک"]
				],
																[
				['text'=>"📍 پشتیبانی"],['text'=>"🔖 راهنما"],['text'=>"🤖 درباره ربات"]
				],
				
 	],
            	'resize_keyboard'=>true
       		])
    		]);
}
else
{
	sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"سلام😉
	
حالت چطوره ؟ $first_name

به ربات چت ناشناس خوش اومدی🌹

به وسیله این ربات میتونی با دیگران به صورت ناشناس چت کنی 😍

13HACK - @tmsizdah

✨جنسیت خودت رو انتخاب کن",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"👱🏻‍ دخترم"],['text'=>"👱🏻 پسرم"]
				],
 	],
            	'resize_keyboard'=>true
       		])
    		]);
$user = json_decode(file_get_contents("data/user.json"),true);	
$user["userfild"]["$from_id"]["numchat"]="4";
$user["userfild"]["$from_id"]["member"]="0";
$user["userfild"]["$from_id"]["like"]="0";
$user["userfild"]["$from_id"]["deslike"]="0";
$user["userfild"]["$from_id"]["vip"]="false";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
}
elseif(strpos($textmassage , '/start ') !== false  ) {
$start = str_replace("/start ","",$textmassage);
if(in_array($from_id, $user["userlist"]) == true && is_numeric($start)) {
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"شما قبلا به ربات دعوت شده ایده ✔️",
    		]);
}
else 
{
if (is_numeric($start)){
@$user = json_decode(file_get_contents("data/user.json"),true);
$member = $user["userfild"]["$start"]["member"];
$plusmember = $member +1;
	sizdahorg('sendmessage',[
	'chat_id'=>$start,
	'text'=>"یک کابر با لینک دعوت شما وارد ربات شد ✔️
📌 تعداد افرادی که دعوت کرده اید : $plusmember",
    		]);
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"سلام😉
	
حالت چطوره ؟ $first_name

به ربات چت ناشناس خوش اومدی🌹

به وسیله این ربات میتونی با دیگران به صورت ناشناس چت کنی😍
13HACK - @tmsizdah
✨جنسیت خودت رو انتخاب کن",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"👱🏻‍ دخترم"],['text'=>"👱🏻 پسرم"]
				],
 	],
            	'resize_keyboard'=>true
       		])
    		]);
$user["userfild"]["$start"]["member"]="$plusmember";
$user["userfild"]["$from_id"]["numchat"]="4";
$user["userfild"]["$from_id"]["member"]="0";
$user["userfild"]["$from_id"]["like"]="0";
$user["userfild"]["$from_id"]["deslike"]="0";
$user["userfild"]["$from_id"]["vip"]="false";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
else
{
$id = base64_decode($start);
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"📍 درخواست چت با طرف مقابل ارسال شده در صورت تایید فرد وارد چت میشوید",
    		]);
sizdahorg('sendmessage',[
	'chat_id'=>$id,
	'text'=>"📍 فردی با نام $name :
	
📌 درخواست چت با شما را دارد 

از دکمه های زیر استفاده کنید 🔻",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"✅ قبول درخواست"],['text'=>"❌ رد درخواست"]
				],
 	],
            	'resize_keyboard'=>true
       		])
    		]);
$user["userfild"]["$from_id"]["idchat"]="$id";
$user["userfild"]["$id"]["idchat"]="$from_id";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
}
}
elseif($textmassage == "✅ قبول درخواست") {
$idchat = $user["userfild"]["$from_id"]["idchat"];
$getuserprofile = getUserProfilePhotos($token,$idchat);
$cuphoto = $getuserprofile->total_count;
$getuserphoto = $getuserprofile->photos[0][0]->file_id;
$getuserprofile2 = getUserProfilePhotos($token,$from_id);
$cuphoto2 = $getuserprofile2->total_count;
$getuserphoto2 = $getuserprofile2->photos[0][0]->file_id;
$like = $user["userfild"]["$idchat"]["like"];
$deslike = $user["userfild"]["$idchat"]["deslike"];
$like2 = $user["userfild"]["$from_id"]["like"];
$deslike2 = $user["userfild"]["$from_id"]["deslike"];
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :
	
چت اغاز شد ✅
13HACK - @tmsizdah
به طرف مقابل احوال پرسی کن 😃",
'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"✂️ پایان چت"],['text'=>"🛑 گزارش تخلف"]
				],
[				
				['text'=>"👁 نمایش اطلاعات"],['text'=>"🚫 بلاکش کن"]
				],
												[				
				['text'=>"▶️ نفر بعدی"],['text'=>"👫 اضافه کردن به دوستان"]
				],
 	],
            	'resize_keyboard'=>true
       		])
    		]);
  sizdahorg('sendphoto',[
  'chat_id'=>$chat_id,
'photo'=>$getuserphoto,
  'caption'=>"❤️ عکس پروفایل طرف مقابلت لایک داره یا نه ؟",
   'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"($like)👍",'callback_data'=>"like"],['text'=>"($deslike)👎",'callback_data'=>"deslike"]
	],
	],
        ])
   ]);
sizdahorg('sendmessage',[
	'chat_id'=>$idchat,
	'text'=>"🤖 پیام سیستم :

درخواست چت توسط طرف مقابل پذیرفته شد✅

به طرف مقابل احوال پرسی کن 😃",
'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"✂️ پایان چت"],['text'=>"🛑 گزارش تخلف"]
				],	
				[				
				['text'=>"👁 نمایش اطلاعات"],['text'=>"🚫 بلاکش کن"]
				],
												[				
				['text'=>"▶️ نفر بعدی"],['text'=>"👫 اضافه کردن به دوستان"]
				],
 	],
            	'resize_keyboard'=>true
       		])
    		]);
			  sizdahorg('sendphoto',[
  'chat_id'=>$idchat,
'photo'=>$getuserphoto2,
  'caption'=>"❤️ عکس پروفایل طرف مقابلت لایک داره یا نه ؟",
   'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"($like2)👍",'callback_data'=>"like"],['text'=>"($deslike2)👎",'callback_data'=>"deslike"]
	],
	],
        ])
   ]);
$user["userfild"]["$from_id"]["chat"]="true";
$user["userfild"]["$idchat"]["chat"]="true";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
elseif($textmassage=="❌ رد درخواست" && $tc == "private"){
$idchat = $user["userfild"]["$from_id"]["idchat"];
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"به منوی اصلی ربات خوش امدید🎉

🔻 از دکمه های زیر استفاده کنید 🔻",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
			[
				['text'=>"💬 چت ناشناس"]
				],
								[
				['text'=>"🏅 حساب ویژه"],['text'=>"💎 اطلاعات حساب|ویرایش"]
				],
												[
				['text'=>"👫 لیست دوستان"],['text'=>"🚫 لیست بلاک"]
				],
																[
				['text'=>"📍 پشتیبانی"],['text'=>"🔖 راهنما"],['text'=>"🤖 درباره ربات"]
				],
				
 	],
            	'resize_keyboard'=>true
       		])
    		]);
			sizdahorg('sendmessage',[
				'chat_id'=>$idchat,
	'text'=>"📍 درخواست چت شما از طرف $first_name رد شد",
    		]);
$user["userfild"]["$from_id"]["chat"]="false";
$user["userfild"]["$idchat"]["chat"]="false";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
elseif($textmassage=="👱🏻‍ دخترم" or $textmassage=="👱🏻 پسرم"){
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"جنسیتت با موفقیت ذخیره شد ✔️

🚦سن خودت رو انتخاب کن",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"13"],['text'=>"14"],['text'=>"15"],['text'=>"16"]
				],
								[
				['text'=>"17"],['text'=>"18"],['text'=>"19"],['text'=>"20"]
				],
								[
				['text'=>"21"],['text'=>"22"],['text'=>"23"],['text'=>"24"]
				],
								[
				['text'=>"25"],['text'=>"26"],['text'=>"27"],['text'=>"28"]
				],
								[
				['text'=>"29"],['text'=>"30"],['text'=>"31"],['text'=>"32"]
				],
								[
				['text'=>"32 +"]
				],
				
 	],
            	'resize_keyboard'=>true
       		])
    		]);
$az = array("👱🏻‍ دخترم","👱🏻 پسرم");
$be = array("دختر","پسر");
$text = str_replace($az,$be,$textmassage);
$user["userfild"]["$from_id"]["sex"]="$text";
$user["userfild"]["$from_id"]["step"]="age";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
elseif($user["userfild"]["$from_id"]["step"] == "age" && $tc == "private"){
if ($textmassage <= 50 && $textmassage >= 14){
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"سن شما با موفقیت ذخیره شد ✔️

🔻 استان خود را انتخاب کنید 🔻",
 'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"آذربایجان شرقی"],['text'=>"اردبیل"],['text'=>"اصفهان"]
				],
								[
				['text'=>"آذربایجان غربی"],['text'=>"البرز"],['text'=>"بوشهر"]
				],
								[
				['text'=>"چهارمحال و بختیاری"],['text'=>"تهران"],['text'=>"ایلام"]
				],
								[
				['text'=>"خراسان جنوبی"],['text'=>"خوزستان"],['text'=>"زنجان"]
				],
								[
				['text'=>"خراسان شمالی"],['text'=>"سمنان"],['text'=>"فارس"]
				],
								[
				['text'=>"خراسان رضوی"],['text'=>"قزوین"],['text'=>"قم"]
				],
												[
				['text'=>"سیستان و بلوچستان"],['text'=>"کردستان"],['text'=>"کرمان"]
				],
																[
				['text'=>"کهگیلویه و بویراحمد"],['text'=>"کرمانشاه"],['text'=>"گیلان"]
				],
																				[
				['text'=>"گلستان"],['text'=>"لرستان"],['text'=>"مازندران"]
				],
																								[
				['text'=>"مرکزی"],['text'=>"هرمزگان"],['text'=>"همدان"],['text'=>"یزد"]
				],
				
 	],
            	'resize_keyboard'=>true
       		])
    		]);
$user["userfild"]["$from_id"]["age"]="$textmassage";
$user["userfild"]["$from_id"]["step"]="city";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
}
elseif($user["userfild"]["$from_id"]["step"] == "city" && $tc == "private"){
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"استان شما با موفقیت ذخیره شد ✔️

به منوی اصلی ربات خوش امدید🎉

🔻 از دکمه های زیر استفاده کنید 🔻",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"💬 چت ناشناس"]
				],
								[
				['text'=>"🏅 حساب ویژه"],['text'=>"💎 اطلاعات حساب|ویرایش"]
				],
												[
				['text'=>"👫 لیست دوستان"],['text'=>"🚫 لیست بلاک"]
				],
																[
				['text'=>"📍 پشتیبانی"],['text'=>"🔖 راهنما"],['text'=>"🤖 درباره ربات"]
				],
				
 	],
            	'resize_keyboard'=>true
       		])
    		]);
$user["userfild"]["$from_id"]["city"]="$textmassage";
$user["userfild"]["$from_id"]["step"]="none";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
elseif($textmassage=="💬 چت ناشناس" && $tc == "private"){
if($tch == 'member' or $tch == 'creator' or $tch == 'administrator'){
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"به بخش چت ناشناس خوش اومدی 💭
	
لطفا با یکی از ویژگی های زیر شروع به چت ناشناس کنید ✔️",
   'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"👤 فرقی نداره"],['text'=>"👫 هم سن"]
				],
												[
				['text'=>"👱🏻 پسر"],['text'=>"👱🏻‍♀️ دختر"]
				],	
												[
				['text'=>"📍 چت با gps [نزدیک]"],['text'=>"🏢 چت با همشهری"]
				],					
																[
				['text'=>"🔙 برگشت"]
				],		
 	],
            	'resize_keyboard'=>true
       		])
    		]);
$user["listchat"][]="$from_id";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
else
{
				sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"کاربر عزیز شما در کانال ربات نیستید و امکان استفاده از چت ناشناس را ندارید ⚠️
	
⭕️ لطفا در کانال زیر عضو شوید :

🆔 @$channel

سپس به ربات برگشته و مجدد امتحان کنید ✔️",
'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"📍 عضوت در کانال",'url'=>"https://t.me/$channel"]
	],
              ]
        ])
    		]);	
}
}
elseif($textmassage=="👤 فرقی نداره" or $textmassage=="🗣 شروع چت" && $tc == "private"){
$vip = $user["userfild"]["$from_id"]["vip"];
$numchat = $user["userfild"]["$from_id"]["numchat"];
if ($vip == "false") {
if ($numchat > 0){
$listchat = $user["listchat"];
$randomchat = $listchat[rand(0,count($listchat)-1)];
if ($randomchat != "" && $randomchat != $from_id){
$getuserprofile = getUserProfilePhotos($token,$randomchat);
$cuphoto = $getuserprofile->total_count;
$getuserphoto = $getuserprofile->photos[0][0]->file_id;
$getuserprofile2 = getUserProfilePhotos($token,$from_id);
$cuphoto2 = $getuserprofile2->total_count;
$getuserphoto2 = $getuserprofile2->photos[0][0]->file_id;
$like = $user["userfild"]["$randomchat"]["like"];
$deslike = $user["userfild"]["$randomchat"]["deslike"];
$like2 = $user["userfild"]["$from_id"]["like"];
$deslike2 = $user["userfild"]["$from_id"]["deslike"];
			sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :

کابر با موفقیت یافت شد ✅

⭕️ قوانین چت :
1️⃣از ارسال کلمات رکیک خودداری کنید
2️⃣از ارسال تبلیغات خودداری کنید
3️⃣در کمال ارامش به گفت گو ناشناس بپردازید و از دادن اطلاعات خود داری کنید
4️⃣از توهین یا بستن چت بیهوده خود داری کنید

⚠️ در صورت رعایت نکردن هر یک از موارد بالا از ربات مسدود خواهید شد

به طرف مقابل احوال پرسی کن 😃",
'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"✂️ پایان چت"],['text'=>"🛑 گزارش تخلف"]
				],
[				
				['text'=>"👁 نمایش اطلاعات"],['text'=>"🚫 بلاکش کن"]
				],
												[				
				['text'=>"▶️ نفر بعدی"],['text'=>"👫 اضافه کردن به دوستان"]
				],
 	],
            	'resize_keyboard'=>true
       		])
    		]);
			  sizdahorg('sendphoto',[
  'chat_id'=>$chat_id,
'photo'=>$getuserphoto,
  'caption'=>"❤️ عکس پروفایل طرف مقابلت لایک داره یا نه ؟",
   'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"($like)👍",'callback_data'=>"like"],['text'=>"($deslike)👎",'callback_data'=>"deslike"]
	],
	],
        ])
   ]);
						sizdahorg('sendmessage',[
	'chat_id'=>$randomchat,
	'text'=>"🤖 پیام سیستم :

کابر با موفقیت یافت شد ✅

⭕️ قوانین چت :
1️⃣از ارسال کلمات رکیک خودداری کنید
2️⃣از ارسال تبلیغات خودداری کنید
3️⃣در کمال ارامش به گفت گو ناشناس بپردازید و از دادن اطلاعات خود داری کنید
4️⃣از توهین یا بستن چت بیهوده خود داری کنید

⚠️ در صورت رعایت نکردن هر یک از موارد بالا از ربات مسدود خواهید شد

به طرف مقابل احوال پرسی کن 😃",
'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"✂️ پایان چت"],['text'=>"🛑 گزارش تخلف"]
				],
[				
				['text'=>"👁 نمایش اطلاعات"],['text'=>"🚫 بلاکش کن"]
				],
												[				
				['text'=>"▶️ نفر بعدی"],['text'=>"👫 اضافه کردن به دوستان"]
				],
 	],
            	'resize_keyboard'=>true
       		])
    		]);
						  sizdahorg('sendphoto',[
  'chat_id'=>$randomchat,
'photo'=>$getuserphoto2,
  'caption'=>"❤️ عکس پروفایل طرف مقابلت لایک داره یا نه ؟",
   'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"($like2)👍",'callback_data'=>"like"],['text'=>"($deslike2)👎",'callback_data'=>"deslike"]
	],
	],
        ])
   ]);
$numberchat = $user["userfild"]["$from_id"]["numchat"];
$plusnumberchat = $numberchat - 1 ;
$user["userfild"]["$from_id"]["numchat"]="$plusnumberchat";
$numberchat2 = $user["userfild"]["$randomchat"]["numchat"];
$plusnumberchat2 = $numberchat2 - 1 ;
$user["userfild"]["$randomchat"]["numchat"]="$plusnumberchat2";
$user["userfild"]["$randomchat"]["idchat"]="$from_id";
$user["userfild"]["$from_id"]["idchat"]="$randomchat";
$user["userfild"]["$from_id"]["chat"]="true";
$user["userfild"]["$randomchat"]["chat"]="true";
$from = array_search($from_id,$user["listchat"]);
$chater = array_search($randomchat,$user["listchat"]);
unset($user["listchat"]["$from"]);
unset($user["listchat"]["$chater"]);
$user["listchat"] = array_values($user["listchat"]); 
$user = json_encode($user,true);
file_put_contents("data/user.json",$user); 
}
else 
{
	sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :

⚠️اتصال بر قرار نشد !

🔖احتمال دارد :
1️⃣کاربر از چت انصراف داده باشد
2️⃣تعداد کاربران در صف کم باشد و کاربران در چت نشناس باشند

🔍 شما در صف انتظار قرار دارید سیستم ما به صورت خودکار شمارا به کاربری متصل خواهد کرد برای اغاز چت سریع تر میتوانید دوباره امتحان کنید

🔆 لطفا دوباره امتحان  کنید",
	]);
}
}
else
{
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"میزان فرصت چت شما به پایان رسید 😞
	
🤖لطفا نسبت به ارتقا ربات خود اقدام کنید",
'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"⭐️ دعوت دوستان",'callback_data'=>"vip"]
	],
		[
	['text'=>"💎 پرداخت هزینه",'callback_data'=>"by"]
	],
	],
        ])
    		]);

}
}
else
{
$user["listchat"][]="$from_id";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
$randomchat = $listchat[rand(0,count($listchat)-1)];
if ($randomchat != "" && $randomchat != $from_id){
$getuserprofile = getUserProfilePhotos($token,$randomchat);
$cuphoto = $getuserprofile->total_count;
$getuserphoto = $getuserprofile->photos[0][0]->file_id;
$getuserprofile2 = getUserProfilePhotos($token,$from_id);
$cuphoto2 = $getuserprofile2->total_count;
$getuserphoto2 = $getuserprofile2->photos[0][0]->file_id;
$like = $user["userfild"]["$randomchat"]["like"];
$deslike = $user["userfild"]["$randomchat"]["deslike"];
$like2 = $user["userfild"]["$from_id"]["like"];
$deslike2 = $user["userfild"]["$from_id"]["deslike"];
			sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :

کابر با موفقیت یافت شد ✅

⭕️ قوانین چت :
1️⃣از ارسال کلمات رکیک خودداری کنید
2️⃣از ارسال تبلیغات خودداری کنید
3️⃣در کمال ارامش به گفت گو ناشناس بپردازید و از دادن اطلاعات خود داری کنید
4️⃣از توهین یا بستن چت بیهوده خود داری کنید

⚠️ در صورت رعایت نکردن هر یک از موارد بالا از ربات مسدود خواهید شد

به طرف مقابل احوال پرسی کن 😃",
'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"✂️ پایان چت"],['text'=>"🛑 گزارش تخلف"]
				],
[				
				['text'=>"👁 نمایش اطلاعات"],['text'=>"🚫 بلاکش کن"]
				],
												[				
				['text'=>"▶️ نفر بعدی"],['text'=>"👫 اضافه کردن به دوستان"]
				],
 	],
            	'resize_keyboard'=>true
       		])
    		]);
			  sizdahorg('sendphoto',[
  'chat_id'=>$chat_id,
'photo'=>$getuserphoto,
  'caption'=>"❤️ عکس پروفایل طرف مقابلت لایک داره یا نه ؟",
   'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"($like)👍",'callback_data'=>"like"],['text'=>"($deslike)👎",'callback_data'=>"deslike"]
	],
	],
        ])
   ]);
						sizdahorg('sendmessage',[
	'chat_id'=>$randomchat,
	'text'=>"🤖 پیام سیستم :

کابر با موفقیت یافت شد ✅

⭕️ قوانین چت :
1️⃣از ارسال کلمات رکیک خودداری کنید
2️⃣از ارسال تبلیغات خودداری کنید
3️⃣در کمال ارامش به گفت گو ناشناس بپردازید و از دادن اطلاعات خود داری کنید
4️⃣از توهین یا بستن چت بیهوده خود داری کنید

⚠️ در صورت رعایت نکردن هر یک از موارد بالا از ربات مسدود خواهید شد

به طرف مقابل احوال پرسی کن 😃",
'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"✂️ پایان چت"],['text'=>"🛑 گزارش تخلف"]
				],
[				
				['text'=>"👁 نمایش اطلاعات"],['text'=>"🚫 بلاکش کن"]
				],
												[				
				['text'=>"▶️ نفر بعدی"],['text'=>"👫 اضافه کردن به دوستان"]
				],
 	],
            	'resize_keyboard'=>true
       		])
    		]);
						  sizdahorg('sendphoto',[
  'chat_id'=>$randomchat,
'photo'=>$getuserphoto2,
  'caption'=>"❤️ عکس پروفایل طرف مقابلت لایک داره یا نه ؟",
   'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"($like2)👍",'callback_data'=>"like"],['text'=>"($deslike2)👎",'callback_data'=>"deslike"]
	],
	],
        ])
   ]);
$numberchat2 = $user["userfild"]["$randomchat"]["numchat"];
$plusnumberchat2 = $numberchat2 - 1 ;
$user["userfild"]["$randomchat"]["numchat"]="$plusnumberchat2";
$user["userfild"]["$randomchat"]["idchat"]="$from_id";
$user["userfild"]["$from_id"]["idchat"]="$randomchat";
$user["userfild"]["$from_id"]["chat"]="true";
$user["userfild"]["$randomchat"]["chat"]="true";
$from = array_search($from_id,$user["listchat"]);
$chater = array_search($randomchat,$user["listchat"]);
unset($user["listchat"]["$from"]);
unset($user["listchat"]["$chater"]);
$user["listchat"] = array_values($user["listchat"]); 
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);  
}
else
{
	sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :

⚠️اتصال بر قرار نشد !

🔖احتمال دارد :
1️⃣کاربر از چت انصراف داده باشد
2️⃣تعداد کاربران در صف کم باشد و کاربران در چت نشناس باشند

🔍 شما در صف انتظار قرار دارید سیستم ما به صورت خودکار شمارا به کاربری متصل خواهد کرد برای اغاز چت سریع تر میتوانید دوباره امتحان کنید

🔆 لطفا دوباره امتحان  کنید",
	]);
}
}
}
elseif($textmassage=="👫 هم سن" or $textmassage=="👱🏻‍♀️ دختر" or $textmassage=="👱🏻 پسر" or $textmassage=="🏢 چت با همشهری" && $tc == "private"){
$vip = $user["userfild"]["$from_id"]["vip"];
if ($vip == "true") {
$listchat = $user["listchat"];
$randomchat = $listchat[rand(0,count($listchat)-1)];
if ($randomchat != "" && $randomchat != $from_id){
$sex = $user["userfild"]["$from_id"]["sex"];
$age = $user["userfild"]["$from_id"]["age"];
$city = $user["userfild"]["$from_id"]["city"];
$sex2 = $user["userfild"]["$randomchat"]["sex"];
$age2 = $user["userfild"]["$randomchat"]["age"];
$city2 = $user["userfild"]["$randomchat"]["city"];
$az = array("👫 هم سن","🏢 چت با همشهری");
$sexarray = array("👱🏻‍♀️ دختر","👱🏻 پسر");
$be = array("$age","$city");
$be2 = array("$age2","$city2");
$insex = array("دختر","پسر");
$set1 = str_replace($az,$be,$textmassage);
$set2 = str_replace($az,$be2,$textmassage);
$setsex = str_replace($sexarray,$insex,$textmassage);
if($set1 == $set2 or $setsex == $sex2){
$getuserprofile = getUserProfilePhotos($token,$randomchat);
$cuphoto = $getuserprofile->total_count;
$getuserphoto = $getuserprofile->photos[0][0]->file_id;
$getuserprofile2 = getUserProfilePhotos($token,$from_id);
$cuphoto2 = $getuserprofile2->total_count;
$getuserphoto2 = $getuserprofile2->photos[0][0]->file_id;
$like = $user["userfild"]["$randomchat"]["like"];
$deslike = $user["userfild"]["$randomchat"]["deslike"];
$like2 = $user["userfild"]["$from_id"]["like"];
$deslike2 = $user["userfild"]["$from_id"]["deslike"];
			sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :

کابر با موفقیت یافت شد ✅

⭕️ قوانین چت :
1️⃣از ارسال کلمات رکیک خودداری کنید
2️⃣از ارسال تبلیغات خودداری کنید
3️⃣در کمال ارامش به گفت گو ناشناس بپردازید و از دادن اطلاعات خود داری کنید
4️⃣از توهین یا بستن چت بیهوده خود داری کنید

⚠️ در صورت رعایت نکردن هر یک از موارد بالا از ربات مسدود خواهید شد

به طرف مقابل احوال پرسی کن 😃",
'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"✂️ پایان چت"],['text'=>"🛑 گزارش تخلف"]
				],
[				
				['text'=>"👁 نمایش اطلاعات"],['text'=>"🚫 بلاکش کن"]
				],
												[				
				['text'=>"▶️ نفر بعدی"],['text'=>"👫 اضافه کردن به دوستان"]
				],
 	],
            	'resize_keyboard'=>true
       		])
    		]);
			  sizdahorg('sendphoto',[
  'chat_id'=>$chat_id,
'photo'=>$getuserphoto,
  'caption'=>"❤️ عکس پروفایل طرف مقابلت لایک داره یا نه ؟",
   'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"($like)👍",'callback_data'=>"like"],['text'=>"($deslike)👎",'callback_data'=>"deslike"]
	],
	],
        ])
   ]);
						sizdahorg('sendmessage',[
	'chat_id'=>$randomchat,
	'text'=>"🤖 پیام سیستم :

کابر با موفقیت یافت شد ✅

⭕️ قوانین چت :
1️⃣از ارسال کلمات رکیک خودداری کنید
2️⃣از ارسال تبلیغات خودداری کنید
3️⃣در کمال ارامش به گفت گو ناشناس بپردازید و از دادن اطلاعات خود داری کنید
4️⃣از توهین یا بستن چت بیهوده خود داری کنید

⚠️ در صورت رعایت نکردن هر یک از موارد بالا از ربات مسدود خواهید شد

به طرف مقابل احوال پرسی کن 😃",
'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"✂️ پایان چت"],['text'=>"🛑 گزارش تخلف"]
				],
[				
				['text'=>"👁 نمایش اطلاعات"],['text'=>"🚫 بلاکش کن"]
				],
												[				
				['text'=>"▶️ نفر بعدی"],['text'=>"👫 اضافه کردن به دوستان"]
				],
 	],
            	'resize_keyboard'=>true
       		])
    		]);
						  sizdahorg('sendphoto',[
  'chat_id'=>$randomchat,
'photo'=>$getuserphoto2,
  'caption'=>"❤️ عکس پروفایل طرف مقابلت لایک داره یا نه ؟",
   'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"($like2)👍",'callback_data'=>"like"],['text'=>"($deslike2)👎",'callback_data'=>"deslike"]
	],
	],
        ])
   ]);
$numberchat2 = $user["userfild"]["$randomchat"]["numchat"];
$plusnumberchat2 = $numberchat2 - 1 ;
$user["userfild"]["$randomchat"]["numchat"]="$plusnumberchat2";
$user["userfild"]["$randomchat"]["idchat"]="$from_id";
$user["userfild"]["$from_id"]["idchat"]="$randomchat";
$user["userfild"]["$from_id"]["chat"]="true";
$user["userfild"]["$randomchat"]["chat"]="true";
$from = array_search($from_id,$user["listchat"]);
$chater = array_search($randomchat,$user["listchat"]);
unset($user["listchat"]["$from"]);
unset($user["listchat"]["$chater"]);
$user["listchat"] = array_values($user["listchat"]); 
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);  
}
else 
{
	sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :

⚠️اتصال بر قرار نشد !

🔖احتمال دارد :
1️⃣کاربر از چت انصراف داده باشد
2️⃣تعداد کاربران در صف کم باشد و کاربران در چت نشناس باشند

🔍 شما در صف انتظار قرار دارید سیستم ما به صورت خودکار شمارا به کاربری متصل خواهد کرد برای اغاز چت سریع تر میتوانید دوباره امتحان کنید

🔆 لطفا دوباره امتحان  کنید",
	]);
	
}
}
else
{
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :

⚠️اتصال بر قرار نشد !

🔖احتمال دارد :
1️⃣کاربر از چت انصراف داده باشد
2️⃣تعداد کاربران در صف کم باشد و کاربران در چت نشناس باشند
3️⃣ کاربر یافت شده اما با شرایط انتخاب شما یکی نباشد !

🔍 شما در صف انتظار قرار دارید سیستم ما به صورت خودکار شمارا به کاربری متصل خواهد کرد برای اغاز چت سریع تر میتوانید دوباره امتحان کنید

🔆 لطفا دوباره امتحان  کنید",
	]);

}
}
else
{
	sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"ربات در این قسمت برای شما ویژه نمیباشد 😞
	
🤖لطفا نسبت به ارتقا ربات خود اقدام کنید",
'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"⭐️ دعوت دوستان",'callback_data'=>"vip"]
	],
		[
	['text'=>"💎 پرداخت هزینه",'callback_data'=>"by"]
	],
	],
        ])
    		]);
}
}
elseif($textmassage=="📍 چت با gps [نزدیک]" && $tc == "private"){
$vip = $user["userfild"]["$from_id"]["vip"];
$member = $user["userfild"]["$from_id"]["member"];
if ($vip == "true" && $member >= 5) {
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"ابتدا باید مکان خود را ارسال کنید🔍

ℹ️ راهنما :
📍 با استفاده از دکمه زیر درخواست ارسال موقغیت مکانی کنید سپس با ورود به نقشه  موقعیت خود را اتتخاب کنید یا باستفاده از روشن کردن GPS [مکان] بگزارید تا خودکار مکان شما در نقشه پیدا شود",
'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"🏚 ارسال موقعیت","request_location" =>true],['text'=>"🔙 برگشت"]
				],	
 	],
            	'resize_keyboard'=>true
       		])
    		]);
$user["userfild"]["$from_id"]["step"]="sencloc";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
else
{
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"ربات در این قسمت برای شما ویژه نمیباشد 😞
	
🤖لطفا نسبت به ارتقا ربات خود اقدام کنید

📍 تعداد افرادی که دعوت کرده اید : $adds
ℹ️ تعداد افراد مورد نیاز بیش از 5 نفر زیر مجموعه است",
'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"⭐️ دعوت دوستان",'callback_data'=>"vip"]
	],
		[
	['text'=>"💎 پرداخت هزینه",'callback_data'=>"by"]
	],
	],
        ])
    		]);

}
}
elseif($user["userfild"]["$from_id"]["step"] == "sendloc" && $tc == "private"){   
if($update->message->location){	
$rand = rand(4,30);
$rand2 = rand(1,10);
			sizdahorg('sendmessage',[       
			'chat_id'=>$chat_id,
			'text'=>"📍 مکان شما در سیستم ذخیره شد در حال جست جو ...",
	]);	
			sizdahorg('sendmessage',[       
			'chat_id'=>$chat_id,
			'text'=>"🤖 پیام سیستم :

کابر با موفقیت یافت شد ✅

⭕️ قوانین چت :
1️⃣از ارسال کلمات رکیک خودداری کنید
2️⃣از ارسال تبلیغات خودداری کنید
3️⃣در کمال ارامش به گفت گو ناشناس بپردازید و از دادن اطلاعات خود داری کنید
4️⃣از توهین یا بستن چت بیهوده خود داری کنید

⚠️در صورت رعایت نکردن هر یک از موارد بالا از ربات مسدود خواهید شد

برای شروع چت از دکمه زیر استفاده کنید🔻

ℹ️ فاصله شما تا فرد : $rand.$rand2 KM",
 'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"🗣 شروع چت"]
				],
								[
				['text'=>"🔙 برگشت"]
				],		
 	],
            	'resize_keyboard'=>true
       		])
	]);	
$user["userfild"]["$from_id"]["step"]="none";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
	}
	}
elseif($textmassage=="🔙 برگشت" && $tc == "private"){
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"به منوی اصلی ربات خوش امدید🎉

🔻 از دکمه های زیر استفاده کنید 🔻",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
			[
				['text'=>"💬 چت ناشناس"]
				],
								[
				['text'=>"🏅 حساب ویژه"],['text'=>"💎 اطلاعات حساب|ویرایش"]
				],
												[
				['text'=>"👫 لیست دوستان"],['text'=>"🚫 لیست بلاک"]
				],
																[
				['text'=>"📍 پشتیبانی"],['text'=>"🔖 راهنما"],['text'=>"🤖 درباره ربات"]
				],
				
 	],
            	'resize_keyboard'=>true
       		])
    		]);
$user["userfild"]["$from_id"]["chat"]="false";
$user["userfild"]["$from_id"]["step"]="none";
$from = array_search($from_id,$user["listchat"]);
unset($user["listchat"]["$from"]);
$user["listchat"] = array_values($user["listchat"]); 
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);  
}
elseif($textmassage=="👁 نمایش اطلاعات" && $tc == "private"){
$vip = $user["userfild"]["$from_id"]["vip"];
if ($vip == "true") {
$idchat = $user["userfild"]["$from_id"]["idchat"];
$stat = file_get_contents("https://api.telegram.org/bot$token/getChatMember?chat_id=$idchat&user_id=".$idchat);
$statjson = json_decode($stat, true);
$name = $statjson['result']['user']['first_name'];
$sex = $user["userfild"]["$idchat"]["sex"];
$age = $user["userfild"]["$idchat"]["age"];
$city = $user["userfild"]["$idchat"]["city"];
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم : 
	
🔘 اطلاعات فرد مقابل :

🗣 نام : $name
🙋🏻🙋🏻‍♂️ جنسیت : $sex
📈 سن : $age
🏫 شهر : $city",
    		]);
}
else
{
	sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :
	
🔘 نمایش اطلاعات فرد مقابل فقط برای حساب ویژه است",
    		]);
}
}
elseif($textmassage=="🛑 گزارش تخلف" && $tc == "private"){
$idchat = $user["userfild"]["$from_id"]["idchat"];
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :
	
گزارش تخلف شما برای مدیر ارسال شد ✔️",
    		]);
			sizdahorg('sendmessage',[
				'chat_id'=>$Dev[0],
	'text'=>"🤖 پیام سیستم :
	
⭕️ یک گزارش تخلف جدبد ارسال شد از طرف :

📍مشخصات ارسال کننده :

🔹ایدی : $from_id

🔸یوزرنیم : @$username
➖➖➖
🚷 ایدی فرد خاطی : $idchat
",
    		]);
}
elseif($textmassage=="▶️ نفر بعدی" && $tc == "private"){
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :
	
⚠️ میخوای این گفت گو رو قطع کنی و به یک چت ناشناس دیگه بری ؟",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"✅ اره بریم بعدی"],['text'=>"❌ خیر"]
				],
			
 	],
            	'resize_keyboard'=>true
       		])
    		]);
}
elseif($textmassage=="✂️ پایان چت" && $tc == "private"){
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :
	
⚠️ ایا از اتمام چت اطمینان دارید ؟",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"✅ بله"],['text'=>"❌ خیر"]
				],
			
 	],
            	'resize_keyboard'=>true
       		])
    		]);
}
elseif($textmassage=="❌ خیر" && $tc == "private"){
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :
	
خوب باشه 😉

به چت ناشناست ادامه بده 😃",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"✂️ پایان چت"],['text'=>"🛑 گزارش تخلف"]
				],	
				[				
				['text'=>"👁 نمایش اطلاعات"],['text'=>"🚫 بلاکش کن"]
				],
												[				
				['text'=>"▶️ نفر بعدی"],['text'=>"👫 اضافه کردن به دوستان"]
				],
 	],
            	'resize_keyboard'=>true
       		])
    		]);
}
elseif($textmassage=="🚫 بلاکش کن" && $tc == "private"){
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :
	
⚠️ مطمعنی میخوای این چت رو پایان بدی و دیگه هیچ وقت به این کاربر وصل نشی ؟",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"✅ اره بلاکش کن"],['text'=>"❌ نه گناه داره"]
				],			
 	],
            	'resize_keyboard'=>true
       		])
    		]);
}
elseif($textmassage=="❌ نه گناه داره" && $tc == "private"){
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :
	
خوب باشه 😉

به چت ناشناست ادامه بده 😃",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"✂️ پایان چت"],['text'=>"🛑 گزارش تخلف"]
				],	
				[				
				['text'=>"👁 نمایش اطلاعات"],['text'=>"🚫 بلاکش کن"]
				],
								[				
				['text'=>"▶️ نفر بعدی"],['text'=>"👫 اضافه کردن به دوستان"]
				],
 	],
            	'resize_keyboard'=>true
       		])
    		]);
}
elseif($textmassage=="👫 اضافه کردن به دوستان" && $tc == "private"){
$idchat = $user["userfild"]["$from_id"]["idchat"];
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :
	
به لیست دوستات اضافه شد 😻

به چت ناشناست ادامه بده 😃",
    		]);
$stat = file_get_contents("https://api.telegram.org/bot$token/getChatMember?chat_id=$idchat&user_id=".$idchat);
$statjson = json_decode($stat, true);
$name = $statjson['result']['user']['first_name'];
$id = base64_encode($idchat);
$user["userfild"]["$from_id"]["frindlist"][]="[$name](https://t.me/$usernamebot?start=$id)";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
elseif($textmassage=="✅ بله" && $tc == "private"){
$vip = $user["userfild"]["$from_id"]["vip"];
$idchat = $user["userfild"]["$from_id"]["idchat"];
if ($vip == "false") {
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"چت با موفقیت بسته شد ✔️
	
به منوی اصلی ربات خوش امدید🎉

🔻 از دکمه های زیر استفاده کنید 🔻",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
			[
				['text'=>"💬 چت ناشناس"]
				],
								[
				['text'=>"🏅 حساب ویژه"],['text'=>"💎 اطلاعات حساب|ویرایش"]
				],
												[
				['text'=>"👫 لیست دوستان"],['text'=>"🚫 لیست بلاک"]
				],
																[
				['text'=>"📍 پشتیبانی"],['text'=>"🔖 راهنما"],['text'=>"🤖 درباره ربات"]
				],
				
 	],
            	'resize_keyboard'=>true
       		])
    		]);
			sizdahorg('sendphoto',[
	'chat_id'=>$chat_id,
	'photo'=>"",
	'caption'=>"دوست داری کسایی که باهاشون چت میکنی رو خودت انتخاب کنی ؟😃
یا این که دیگه محدودتی تو چت کردن نداشتی ؟😍
یا بتونی تو چت فیلم یا هر چیزی که دوست داشتی رو ارسال کنی ؟

🤖 ربات خودت رو ویژه کن",
'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"⭐️ دعوت دوستان",'callback_data'=>"vip"]
	],
		[
	['text'=>"💎 پرداخت هزینه",'callback_data'=>"by"]
	],
	],
        ])
    		]);
			sizdahorg('sendmessage',[
	'chat_id'=>$idchat,
	'text'=>"چت توسط طرف مقابل بسته شد ☹️️
	
به منوی اصلی ربات خوش امدید🎉

🔻 از دکمه های زیر استفاده کنید 🔻",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
			[
				['text'=>"💬 چت ناشناس"]
				],
								[
				['text'=>"🏅 حساب ویژه"],['text'=>"💎 اطلاعات حساب|ویرایش"]
				],
												[
				['text'=>"👫 لیست دوستان"],['text'=>"🚫 لیست بلاک"]
				],
																[
				['text'=>"📍 پشتیبانی"],['text'=>"🔖 راهنما"],['text'=>"🤖 درباره ربات"]
				],
				
 	],
            	'resize_keyboard'=>true
       		])
    		]);
			sizdahorg('sendphoto',[
	'chat_id'=>$idchat,
	'photo'=>"",
	'caption'=>"دوست داری کسایی که باهاشون چت میکنی رو خودت انتخاب کنی ؟😃
یا این که دیگه محدودتی تو چت کردن نداشتی ؟😍
یا بتونی تو چت فیلم یا هر چیزی که دوست داشتی رو ارسال کنی ؟

🤖 ربات خودت رو ویژه کن",
'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"⭐️ دعوت دوستان",'callback_data'=>"vip"]
	],
		[
	['text'=>"💎 پرداخت هزینه",'callback_data'=>"by"]
	],
	],
        ])
    		]);
}
else
{
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"چت با موفقیت بسته شد ✔️
	
به منوی اصلی ربات خوش امدید🎉

🔻 از دکمه های زیر استفاده کنید 🔻",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
			[
				['text'=>"💬 چت ناشناس"]
				],
								[
				['text'=>"🏅 حساب ویژه"],['text'=>"💎 اطلاعات حساب|ویرایش"]
				],
												[
				['text'=>"👫 لیست دوستان"],['text'=>"🚫 لیست بلاک"]
				],
																[
				['text'=>"📍 پشتیبانی"],['text'=>"🔖 راهنما"],['text'=>"🤖 درباره ربات"]
				],
				
 	],
            	'resize_keyboard'=>true
       		])
    		]);
			sizdahorg('sendmessage',[
	'chat_id'=>$idchat,
	'text'=>"چت توسط طرف مقابل بسته شد ☹️️
	
به منوی اصلی ربات خوش امدید🎉

🔻 از دکمه های زیر استفاده کنید 🔻",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
			[
				['text'=>"💬 چت ناشناس"]
				],
								[
				['text'=>"🏅 حساب ویژه"],['text'=>"💎 اطلاعات حساب|ویرایش"]
				],
												[
				['text'=>"👫 لیست دوستان"],['text'=>"🚫 لیست بلاک"]
				],
																[
				['text'=>"📍 پشتیبانی"],['text'=>"🔖 راهنما"],['text'=>"🤖 درباره ربات"]
				],
				
 	],
            	'resize_keyboard'=>true
       		])
    		]);
}
$user["userfild"]["$from_id"]["chat"]="false";
$user["userfild"]["$idchat"]["chat"]="false";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
elseif($textmassage=="✅ اره بریم بعدی" && $tc == "private"){
$idchat = $user["userfild"]["$from_id"]["idchat"];
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"چت با موفقیت بسته شد ✔️
	
در لیست انتظار هستید 🎉

🔻 از دکمه های زیر استفاده کنید 🔻",
'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"🗣 شروع چت"]
				],
								[
				['text'=>"🔙 برگشت"]
				],		
 	],
            	'resize_keyboard'=>true
       		])
    		]);
			sizdahorg('sendmessage',[
	'chat_id'=>$idchat,
	'text'=>"چت توسط طرف مقابل بسته شد ☹️️
	
به منوی اصلی ربات خوش امدید🎉

🔻 از دکمه های زیر استفاده کنید 🔻",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
			[
				['text'=>"💬 چت ناشناس"]
				],
								[
				['text'=>"🏅 حساب ویژه"],['text'=>"💎 اطلاعات حساب|ویرایش"]
				],
												[
				['text'=>"👫 لیست دوستان"],['text'=>"🚫 لیست بلاک"]
				],
																[
				['text'=>"📍 پشتیبانی"],['text'=>"🔖 راهنما"],['text'=>"🤖 درباره ربات"]
				],
				
 	],
            	'resize_keyboard'=>true
       		])
    		]);
$user["userfild"]["$from_id"]["chat"]="false";
$user["userfild"]["$idchat"]["chat"]="false";
$user["listchat"][]="$from_id";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
elseif($textmassage=="✅ اره بلاکش کن" && $tc == "private"){
$idchat = $user["userfild"]["$from_id"]["idchat"];
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"چت با موفقیت بسته شد ✔️
	
🚫 کاربر مقابل بلاک شد
	
به منوی اصلی ربات خوش امدید🎉

🔻 از دکمه های زیر استفاده کنید 🔻",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
			[
				['text'=>"💬 چت ناشناس"]
				],
								[
				['text'=>"🏅 حساب ویژه"],['text'=>"💎 اطلاعات حساب|ویرایش"]
				],
												[
				['text'=>"👫 لیست دوستان"],['text'=>"🚫 لیست بلاک"]
				],
																[
				['text'=>"📍 پشتیبانی"],['text'=>"🔖 راهنما"],['text'=>"🤖 درباره ربات"]
				],
				
 	],
            	'resize_keyboard'=>true
       		])
    		]);
			sizdahorg('sendmessage',[
	'chat_id'=>$idchat,
	'text'=>"چت توسط طرف مقابل بسته شد ☹️️
	
🅾️ ای وای اون تورو بلاک کرد مگه چی کار کرده بودی؟
	
به منوی اصلی ربات خوش امدید🎉

🔻 از دکمه های زیر استفاده کنید 🔻",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
			[
				['text'=>"💬 چت ناشناس"]
				],
								[
				['text'=>"🏅 حساب ویژه"],['text'=>"💎 اطلاعات حساب|ویرایش"]
				],
												[
				['text'=>"👫 لیست دوستان"],['text'=>"🚫 لیست بلاک"]
				],
																[
				['text'=>"📍 پشتیبانی"],['text'=>"🔖 راهنما"],['text'=>"🤖 درباره ربات"]
				],
				
 	],
            	'resize_keyboard'=>true
       		])
    		]);
$stat = file_get_contents("https://api.telegram.org/bot$token/getChatMember?chat_id=$idchat&user_id=".$idchat);
$statjson = json_decode($stat, true);
$name = $statjson['result']['user']['first_name'];
$id = base64_encode($idchat);
$user["userfild"]["$from_id"]["blocklist"][]="[$name](https://t.me/$usernamebot?start=$id)";
$user["userfild"]["$from_id"]["chat"]="false";
$user["userfild"]["$idchat"]["chat"]="false";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
elseif($user["userfild"]["$from_id"]["chat"] == "true" && $tc == "private"){
if($textmassage != "✂️ پایان چت" && $textmassage != "✅ قبول درخواست" && $textmassage != "❌ رد درخواست" && $textmassage != "🛑 گزارش تخلف" && $textmassage != "✅ بله" && $textmassage != "❌ خیر" && $textmassage != "👁 نمایش اطلاعات" &&$textmassage != "🚫 بلاکش کن" && $textmassage != "❌ نه گناه داره" && $textmassage != "▶️ نفر بعدی" && $textmassage != "👫 اضافه کردن به دوستان" && $textmassage != "✅ اره بریم بعدی") {
$vip = $user["userfild"]["$from_id"]["vip"];
$idchat = $user["userfild"]["$from_id"]["idchat"];
if ($vip == "false") {
if ($update->message->text) {
sizdahorg('sendmessage',[
	'chat_id'=>$idchat,
	'text'=>"`$textmassage`",
	'parse_mode'=>'MarkDown',
    		]);
}
else
{
	sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🤖 پیام سیستم :
	
⚠️ حساب شما ویژه نسیت و ارسال انواع رسانه امکان پذیر نیست ⚠️",
    		]);
}
}
else
{
$photo = $message->photo;
$file = $photo[count($photo)-1]->file_id;
$get = sizdahorg('getfile',['file_id'=>$file]);
$patch = $get->result->file_path;
file_put_contents("data/photo.png",file_get_contents("https://api.telegram.org/file/bot$token/$patch"));
$voice = $message->voice;
$file = $voice->file_id;
$get = sizdahorg('getfile',['file_id'=>$file]);
$patch = $get->result->file_path;
file_put_contents("data/voice.ogg",file_get_contents("https://api.telegram.org/file/bot$token/$patch"));
$document = $update->message->document;
$file = $document->file_id;
      $get = sizdahorg('getfile',['file_id'=>$file]);
      $patch = $get->result->file_path;
file_put_contents("data/document.gif",file_get_contents("https://api.telegram.org/file/bot$token/$patch"));
$sticker = $update->message->sticker;
$file = $sticker->file_id;
      $get = sizdahorg('getfile',['file_id'=>$file]);
      $patch = $get->result->file_path;
file_put_contents("data/sticker.webp",file_get_contents("https://api.telegram.org/file/bot$token/$patch"));
$audio = $update->message->audio;
$file = $audio->file_id;
      $get = sizdahorg('getfile',['file_id'=>$file]);
      $patch = $get->result->file_path;
file_put_contents("data/audio.mp3",file_get_contents("https://api.telegram.org/file/bot$token/$patch"));
sizdahorg('sendmessage',[
	'chat_id'=>$idchat,
	'text'=>"`$textmassage`",
	'parse_mode'=>'MarkDown',
    		]);
			sizdahorg('sendphoto',[
	'chat_id'=>$idchat,
	'photo'=>new CURLFile("data/photo.png"),
    		]);
						sizdahorg('senddocument',[
	'chat_id'=>$idchat,
	'document'=>new CURLFile("data/document.gif"),
    		]);
									sizdahorg('sendsticker',[
	'chat_id'=>$idchat,
	'sticker'=>new CURLFile("data/sticker.webp"),
    		]);
											sizdahorg('sendvoice',[
	'chat_id'=>$idchat,
	'voice'=>new CURLFile("data/voice.ogg"),
    		]);
														sizdahorg('sendvoice',[
	'chat_id'=>$idchat,
	'voice'=>new CURLFile("data/audio.mp3"),
    		]);
unlink("data/voice.ogg");
unlink("data/sticker.webp");
unlink("data/photo.png");
unlink("data/document.gif");
unlink("data/audio.mp3");
}
}
}
elseif($data=="like"){
$idchat = $user["userfild"]["$fromid"]["idchat"];
$like = $user["userfild"]["$idchat"]["like"];
$pluslike = $like + 1 ;
         sizdahorg('sendmessage',[
             'chat_id'=>$chatid,
  'message_id'=>$messageid,
  'text'=>"📣 حله  یدونه لایک توهم به لایک هاش اضافه شد
👍 لایک هاش : $pluslike",
	]);
	            sizdahorg('deletemessage',[
                'chat_id'=>$chatid,
     'message_id'=>$messageid,
           ]);
$user["userfild"]["$idchat"]["like"]="$pluslike";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);		 
	}
	elseif($data=="deslike"){
$idchat = $user["userfild"]["$fromid"]["idchat"];
$like = $user["userfild"]["$idchat"]["deslike"];
$pluslike = $like + 1 ;
         sizdahorg('sendmessage',[
             'chat_id'=>$chatid,
  'message_id'=>$messageid,
  'text'=>"📣 ای بابا یکی به لایک های منفیش اضافه کردی
👍 لایک های منفیش : $pluslike",
	]);
	            sizdahorg('deletemessage',[
                'chat_id'=>$chatid,
     'message_id'=>$messageid,
           ]);
$user["userfild"]["$idchat"]["deslike"]="$pluslike";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);	
	}
elseif($textmassage=="💎 اطلاعات حساب|ویرایش" && $tc == "private"){
$sex = $user["userfild"]["$from_id"]["sex"];
$age = $user["userfild"]["$from_id"]["age"];
$city = $user["userfild"]["$from_id"]["city"];
$like = $user["userfild"]["$from_id"]["like"];
$deslike = $user["userfild"]["$from_id"]["deslike"];
$member = $user["userfild"]["$from_id"]["member"];
$numchat = $user["userfild"]["$from_id"]["numchat"];
$vip = $user["userfild"]["$from_id"]["vip"];
if ($vip == "true") {
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"📌اطلاعات حساب شما :
➖➖➖➖➖	

1️⃣نام شما : $first_name
2️⃣جنسیت شما : $sex
3️⃣سن شما : $age
4️⃣شهر شما : $city
5️⃣نوع حساب : ویژه
6️⃣تعداد افرادی که دعوت کرده اید : $member
7⃣ تعداد لایک های عکس پروفایل شما : $like
8⃣ تعداد لایک های منفی عکس پروفایل شما : $deslike


➖➖➖➖➖",
 'reply_markup'=>json_encode([
            	'keyboard'=>[
								[
				['text'=>"✏️ ویرایش اطلاعات"],['text'=>"🔙 برگشت"]
				],
				],
				            	'resize_keyboard'=>true
       		])
    		]);
}
else
{
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"📌اطلاعات حساب شما :
➖➖➖➖➖	

1️⃣نام شما : $first_name
2️⃣جنسیت شما : $sex
3️⃣سن شما : $age
4️⃣شهر شما : $city
5️⃣نوع حساب : عادی
6️⃣تعداد افرادی که دعوت کرده اید : $member
7️⃣تعداد فرصت های چت : $numchat
8️⃣ تعداد لایک های عکس پروفایل شما : $like
9️⃣ تعداد لایک های منفی عکس پروفایل شما : $deslike

➖➖➖➖➖",
 'reply_markup'=>json_encode([
            	'keyboard'=>[
								[
				['text'=>"✏️ ویرایش اطلاعات"],['text'=>"🔙 برگشت"]
				],
				],
				            	'resize_keyboard'=>true
       		])
    		]);
}
}
elseif($textmassage=="✏️ ویرایش اطلاعات" && $tc == "private"){
$edit = $user["userfild"]["$from_id"]["edit"];
if ($edit != "true") {
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"📍به قسمت ویرایش اطلاعات خوش امدید

🔖قسمت مورد نظر برای ویرایش را انتخاب کنید

⚠️ توجه این امکان فقط یک بار امکان پذیر است",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
								[
				['text'=>"1️⃣ ویرایش سن"],['text'=>"2️⃣ ویرایش استان"]
				],
								[
['text'=>"3️⃣ ویرایش جنسیت"]
				],
												[
				['text'=>"🔙 برگشت"]
				],
				],
				            	'resize_keyboard'=>true
       		])
			]);
$user["userfild"]["$from_id"]["edit"]="true";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
else
{
	sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"📌 شما یک بار از این قسمت استفاده کرده اید
	
امکان استفاده دوباره وجود نداره",
			]);
}
}
elseif($textmassage=="1️⃣ ویرایش سن" && $tc == "private"){
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"📍 سن خورد را انتخاب کنید",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"13"],['text'=>"14"],['text'=>"15"],['text'=>"16"]
				],
								[
				['text'=>"17"],['text'=>"18"],['text'=>"19"],['text'=>"20"]
				],
								[
				['text'=>"21"],['text'=>"22"],['text'=>"23"],['text'=>"24"]
				],
								[
				['text'=>"25"],['text'=>"26"],['text'=>"27"],['text'=>"28"]
				],
								[
				['text'=>"29"],['text'=>"30"],['text'=>"31"],['text'=>"32"]
				],
								[
				['text'=>"32 +"]
				],
				
 	],
            	'resize_keyboard'=>true
       		])
			]);
$user["userfild"]["$from_id"]["step"]="editage";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
elseif($user["userfild"]["$from_id"]["step"] == "editage" && $tc == "private"){
if ($textmassage <= 50 && $textmassage >= 14){
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"سن شما با موفقیت ذخیره شد ✔️",
 'reply_markup'=>json_encode([
            	'keyboard'=>[
								[
				['text'=>"1️⃣ ویرایش سن"],['text'=>"2️⃣ ویرایش استان"]
				],
								[
				['text'=>"3️⃣ ویرایش جنسیت"]
				],
												[
				['text'=>"🔙 برگشت"]
				],
				],
				            	'resize_keyboard'=>true
       		])
    		]);
$user["userfild"]["$from_id"]["step"]="none";
$user["userfild"]["$from_id"]["age"]="$textmassage";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
}
elseif($textmassage=="2️⃣ ویرایش استان" && $tc == "private"){
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🔻 استان خود را انتخاب کنید 🔻",
'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"آذربایجان شرقی"],['text'=>"اردبیل"],['text'=>"اصفهان"]
				],
								[
				['text'=>"آذربایجان غربی"],['text'=>"البرز"],['text'=>"بوشهر"]
				],
								[
				['text'=>"چهارمحال و بختیاری"],['text'=>"تهران"],['text'=>"ایلام"]
				],
								[
				['text'=>"خراسان جنوبی"],['text'=>"خوزستان"],['text'=>"زنجان"]
				],
								[
				['text'=>"خراسان شمالی"],['text'=>"سمنان"],['text'=>"فارس"]
				],
								[
				['text'=>"خراسان رضوی"],['text'=>"قزوین"],['text'=>"قم"]
				],
												[
				['text'=>"سیستان و بلوچستان"],['text'=>"کردستان"],['text'=>"کرمان"]
				],
																[
				['text'=>"کهگیلویه و بویراحمد"],['text'=>"کرمانشاه"],['text'=>"گیلان"]
				],
																				[
				['text'=>"گلستان"],['text'=>"لرستان"],['text'=>"مازندران"]
				],
																								[
				['text'=>"مرکزی"],['text'=>"هرمزگان"],['text'=>"همدان"],['text'=>"یزد"]
				],
				
 	],
            	'resize_keyboard'=>true
       		])
			]);
$user["userfild"]["$from_id"]["step"]="editcity";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
elseif($user["userfild"]["$from_id"]["step"] == "editcity" && $tc == "private"){
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"استان شما با موفقیت ذخیره شد ✔️",
 'reply_markup'=>json_encode([
            	'keyboard'=>[
								[
				['text'=>"1️⃣ ویرایش سن"],['text'=>"2️⃣ ویرایش استان"]
				],
								[
				['text'=>"3️⃣ ویرایش جنسیت"]
				],
												[
				['text'=>"🔙 برگشت"]
				],
				],
				            	'resize_keyboard'=>true
       		])
    		]);
$user["userfild"]["$from_id"]["step"]="none";
$user["userfild"]["$from_id"]["city"]="$textmassage";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
elseif($textmassage=="3️⃣ ویرایش جنسیت" && $tc == "private"){
	sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🔻 جنسیت خود را انتخاب کنید 🔻",
'reply_markup'=>json_encode([
            	'keyboard'=>[
				[
				['text'=>"دختر"],['text'=>"پسر"]
				],
 	],
            	'resize_keyboard'=>true
       		])
			]);
$user["userfild"]["$from_id"]["step"]="editsex";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
elseif($user["userfild"]["$from_id"]["step"] == "editsex" && $tc == "private"){
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"جنست شما با موفقیت ذخیره شد ✔️",
 'reply_markup'=>json_encode([
            	'keyboard'=>[
								[
				['text'=>"1️⃣ ویرایش سن"],['text'=>"2️⃣ ویرایش استان"]
				],
								[
				['text'=>"3️⃣ ویرایش جنسیت"]
				],
												[
				['text'=>"🔙 برگشت"]
				],
				],
				            	'resize_keyboard'=>true
       		])
    		]);
$user["userfild"]["$from_id"]["step"]="none";
$user["userfild"]["$from_id"]["sex"]="$textmassage";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
elseif($textmassage=="🏅 حساب ویژه" && $tc == "private"){
	sizdahorg('sendphoto',[
	'chat_id'=>$chat_id,
	'photo'=>new CURLFile("data/vip.jpg"),
	'caption'=>"دوست داری کسایی که باهاشون چت میکنی رو خودت انتخاب کنی ؟😃
یا این که دیگه محدودیتی تو چت کردن نداشتی ؟ 😍
یا بتونی تو چت فیلم یا هر چیزی که دوست داشتی رو ارسال کنی ؟
و...

🔻 یکی از روش های زیر را انتخاب کنید 🔻",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
								[
				['text'=>"👥 دعوت دیگران"],['text'=>"💎 پرداخت هزینه"]
				],
								[
				['text'=>"🔙 برگشت"]
				],
				],
				            	'resize_keyboard'=>true
       		])
			]);
}
elseif($textmassage=="🚫 لیست بلاک" && $tc == "private"){
$list = $user["userfild"]["$from_id"]["blocklist"];
for($z = 0;$z <= count($list)-1;$z++){
$result = $result.$list[$z]."\n";
}
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"📍بلاک لیست شما :
➖➖➖➖
$result",
'parse_mode'=>'MarkDown',
'disable_web_page_preview'=>true,
 'reply_markup'=>json_encode([
            	'keyboard'=>[
								[
				['text'=>"🔙 برگشت"],['text'=>"❌ پاک کردن لیست"]
				],
				],
				            	'resize_keyboard'=>true
       		])
			]);
}
elseif($textmassage=="👫 لیست دوستان" && $tc == "private"){
$list = $user["userfild"]["$from_id"]["frindlist"];
for($z = 0;$z <= count($list)-1;$z++){
$result = $result.$list[$z]."\n";
}
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"📍 لیست دوستان شما :
➖➖➖➖
$result",
'parse_mode'=>'MarkDown',
'disable_web_page_preview'=>true,
			]);
}
elseif($textmassage=="❌ پاک کردن لیست" && $tc == "private"){
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"📍 لیست بلاک شما به صورت کامل پاکسازی شد",
     'reply_markup'=>json_encode([
            	'keyboard'=>[
			[
				['text'=>"💬 چت ناشناس"]
				],
								[
				['text'=>"🏅 حساب ویژه"],['text'=>"💎 اطلاعات حساب|ویرایش"]
				],
												[
				['text'=>"👫 لیست دوستان"],['text'=>"🚫 لیست بلاک"]
				],
																[
				['text'=>"📍 پشتیبانی"],['text'=>"🔖 راهنما"],['text'=>"🤖 درباره ربات"]
				],
				
 	],
            	'resize_keyboard'=>true
       		])
			]);
unset($user["userfild"]["$from_id"]["blocklist"]);
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
elseif($textmassage=="/vip" or $textmassage=="👥 دعوت دیگران" && $tc == "private"){
$member = $user["userfild"]["$from_id"]["member"];
$plusmember = 3 - $member ;
			sizdahorg('sendphoto',[
	'chat_id'=>$chat_id,
	'photo'=>new CURLFile("data/vip.jpg"),
	'caption'=>"ربات چت ناشناس با هزاران کاربر😍
وای این ربات عالیه میتونی چت کنی بدون این که بفهمی طرف مقابلت کیه ! 😉

💎منتظر چی هستی وارد لینک ربات شو :
https://t.me/$usernamebot?start=$from_id",
    		]);
			sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"👆🏻 بنر بالا حاوی لینک دعوت شماست ان رو برای دوستان و گروه و کانال خود ارسال کنید و با جمع اوری زیر مجموعه ربات خودتون رو رایگان ویژه کنید 👆🏻",
    		]);
			sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"📌 تعداد افرادی که دعوت کرده اید : $member
	
🔱 تعداد نفراتی که باید دعوت کنید تا ربات ویژه شود : $plusmember",
    		]);
}
elseif($data == "vip"){
$member = $user["userfild"]["$from_id"]["member"];
$plusmember = 3 - $member ;
			sizdahorg('sendphoto',[
	'chat_id'=>$chatid,
	'photo'=>new CURLFile("data/vip.jpg"),
	'caption'=>"ربات چت ناشناس با هزاران کاربر😍
وای این ربات عالیه میتونی چت کنی بدون این که بفهمی طرف مقابلت کیه ! 😉

💎منتظر چی هستی وارد لینک ربات شو :
https://t.me/$usernamebot?start=$fromid",
    		]);
			sizdahorg('sendmessage',[
	'chat_id'=>$chatid,
	'text'=>"👆🏻 بنر بالا حاوی لینک دعوت شماست ان رو برای دوستان و گروه و کانال خود ارسال کنید و با جمع اوری زیر مجموعه ربات خودتون رو رایگان ویژه کنید 👆🏻",
    		]);
			sizdahorg('sendmessage',[
	'chat_id'=>$chatid,
	'text'=>"📌 تعداد افرادی که دعوت کرده اید : $member
	
🔱 تعداد نفراتی که باید دعوت کنید تا ربات ویژه شود : $plusmember",
    		]);
}
elseif($data == "by"){
			sizdahorg('sendmessage',[
	'chat_id'=>$chatid,
	'text'=>"📍 شما با پرداخت 2000 هزار تومان میتوانید حساب خودتون رو ویژه کنید و از امکانات فوق العاده ربات استفاده کنید.
	
لیست امکانات ربات ویژه :

1️⃣ امکان تفکیک بندی چت با طرف مقابل
2️⃣ امکان چت با gps و افراد نزدیک
3️⃣ امکان مشاهده پروفایل طرف مقابل 
4️⃣ امکان چت نامحدود و ...

⭐️ و کلی امکانات فوق العاده دیگه ...

🔴 روی خرید کلیک کرده و در صفحه پرداخت آیدی عددی خود را وارد کنید.
🔵 آیدی شما : $fromid",
'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"🚀 خرید",'url'=>"$web/other/pay.php?amount=2000&callback=$web/other/by-2000.php?id=$fromid"]
	],
              ]
        ])
    		]);
}
elseif($textmassage=="💎 پرداخت هزینه" && $tc == "private"){
			sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"📍 شما با پرداخت 2000 هزار تومن میتوانید حساب خودتون رو ویژه کنید و از امکانات فوق العاده ربات استفاده کنید
	
ℹ️ لیست امکانات ربات ویژه :

1️⃣ امکان تفکیک بندی چت با طرف مقابل
2️⃣ امکان چت با gps و افراد نزدیک
3️⃣ امکان مشاهده پروفایل طرف مقابل 
4️⃣ امکان چت نامحدود و ...

⭐️ و کلی امکانات فوق العاده دیگه ...",
'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"🚀 خرید",'url'=>"$web/other/pay.php?amount=2000&callback=$web/other/by-2000.php?id=$from_id"]
	],
              ]
        ])
    		]);
}
elseif($user["userfild"]["$from_id"]["vip"] == "false"){
if($user["userfild"]["$from_id"]["member"] > 3) {
$member = $user["userfild"]["$from_id"]["member"];
sizdahorg('sendmessage',[
	'chat_id'=>$chat_id,
	'text'=>"🎉 تبریک 🎉

حساب شما ویژه شد ✅
📌تعداد افرادی که دعوت کرده اید : $member",
    		]);
$user["userfild"]["$from_id"]["vip"]="true";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
}
elseif($data=="chatfake"){
$vip = $user["userfild"]["$from_id"]["vip"];
if ($vip != "true") {
	sizdahorg('sendmessage',[
	'chat_id'=>$chatid,
	'text'=>"ربات در این قسمت برای شما ویژه نمیباشد 😞
	
🤖لطفا نسبت به ارتقا ربات خود اقدام کنید",
'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"⭐️ دعوت دوستان",'callback_data'=>"vip"]
	],
		[
	['text'=>"💎 پرداخت هزینه",'callback_data'=>"by"]
	],
	],
        ])
    		]);
}
else
{
	sizdahorg('sendmessage',[
	'chat_id'=>$chatid,
	'text'=>"😇 فعلا تو چت ناشناسه یکم صبر کن و بعد دوباره امتحان کن",
    		]);
}
	}
	elseif($data=="blockfake"){
$vip = $user["userfild"]["$from_id"]["vip"];
if ($vip != "true") {
	sizdahorg('sendmessage',[
	'chat_id'=>$chatid,
	'text'=>"ربات در این قسمت برای شما ویژه نمیباشد 😞
	
🤖لطفا نسبت به ارتقا ربات خود اقدام کنید",
'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"⭐️ دعوت دوستان",'callback_data'=>"vip"]
	],
		[
	['text'=>"💎 پرداخت هزینه",'callback_data'=>"by"]
	],
	],
        ])
    		]);
}
else
{
	sizdahorg('sendmessage',[
	'chat_id'=>$chatid,
	'text'=>"🚫 مسدود شد",
    		]);
}
	}
		elseif($data=="nextfake"){
$vip = $user["userfild"]["$from_id"]["vip"];
if ($vip != "true") {
	sizdahorg('sendmessage',[
	'chat_id'=>$chatid,
	'text'=>"ربات در این قسمت برای شما ویژه نمیباشد 😞
	
🤖لطفا نسبت به ارتقا ربات خود اقدام کنید",
'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"⭐️ دعوت دوستان",'callback_data'=>"vip"]
	],
		[
	['text'=>"💎 پرداخت هزینه",'callback_data'=>"by"]
	],
	],
        ])
    		]);
}
else
{
	sizdahorg('sendmessage',[
	'chat_id'=>$chatid,
	'text'=>"⚠️ کابری پیدا نشد لطفا دوباره امتخان کنید یا بهتر است از دکمه چت ناشناس استفاده کنید",
    		]);
}
	}
if($textmassage=="🤖 درباره ربات" && $tc == "private"){
				sizdahorg('sendmessage',[
		'chat_id'=>$chat_id,
		'text'=>"🤖 ربات واتس اپ | whtasapp (چت ناشناس)
➖➖➖
📍ربات چت ناشاس یک ربات اجتمای است با نام مستعار ربات واتس اپ

🚀 رباتی هوشمند برای چت های دوستانه و لذت بخش برای شما ایرانیان عزیز

📦 برنامه نویسی و کل حقوق این ربات نزده :
tmsizdah
کاملا محفوظ است ! ✅

🆔 @$usernamebot",
	]);
	}
elseif($textmassage=="🔖 راهنما" && $tc == "private"){
				sizdahorg('sendmessage',[
		'chat_id'=>$chat_id,
		'text'=>"🤖 ربات واتس اپ | whtasapp (چت ناشناس)
➖➖➖➖➖
بخش راهنمای ربات خوش امدید 🔆

1️⃣ چت ناشناس : این قسمت برای شروع چت ناشناس است و 6 قسمت دارد 

⚠️ قسمت [فرقی نداره] عمومی است و همه کاربران میتوانند از این قسمت استفاده کنند اما قسمت های غیر از این برای ربات ویژه است

♻️در این قسمت ربات شما را به صورت تصادفی به یک نفر وصل میکند و شما میتوانید به گفت گو بپردازید

⭐️ درقسمت های دیگه چت ناشناس هم بر اساس تفکیک که شما انتخاب کردین به چت ناشناس میپردازید

✨ در قسمت لیست دوستان و لیست بلاک هم میتوانید با ضربه بر روی نام فرد با او ارتباط بر قرار کنید
➖➖➖
ℹ️ در بقیه قسمت های ربات نیز توضیحات کامل وجود دارد با تشکر از توجه شما :) 

🆔 @$usernamebot",
	]);
	}
elseif($textmassage=="📍 پشتیبانی" && $tc == "private"){
				sizdahorg('sendmessage',[
		'chat_id'=>$chat_id,
		'text'=>"نظرات شما باعث دلگرمی ماست❤️
		13HACK - @tmsizdah
➖➖➖➖➖
انتفادات پیشنهادات و نظرات خود را برای ما ارسال کنید✔️
➖➖➖
پیام خود را وارد کنید",
                 'reply_markup'=>json_encode([
	'resize_keyboard'=>true,
	'keyboard'=>[
	[
	['text'=>"🔙 برگشت"]
	],
	]
	])
	]);
$user["userfild"]["$from_id"]["step"]="sup";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
	}
elseif($user["userfild"]["$from_id"]["step"] == "sup" && $tc == "private"){   
if ($textmassage != "🔙 برگشت") {	
sizdahorg('ForwardMessage',[
'chat_id'=>$Dev[0],
'from_chat_id'=>$chat_id,
'message_id'=>$message_id
]);
			sizdahorg('sendmessage',[       
			'chat_id'=>$chat_id,
			'text'=>"✔️نظر شما ارسال شد.\nبا تشکر از شما",
	]);	
	}
	}
elseif($update->message && $rt && $from_id == $Dev[0] && $tc == "private"){
if($update->message->text){
	sizdahorg('sendmessage',[
        "chat_id"=>$chat_id,
        "text"=>"پیام شما برای فرد ارسال شد ✔️"
		]);
	sizdahorg('sendmessage',[
        "chat_id"=>$reply,
        "text"=>"👤پاسخ پشتیبان برای شما :

`$textmassage`",
'parse_mode'=>'MarkDown'
		]);
}
}
elseif(file_get_contents("data/$fromid.txt") == "true"){
	sizdahorg('sendmessage',[
        "chat_id"=>$chat_id,
        "text"=>"در حال تایید حساب ویژه ... ✔️"
		]);
$user["userfild"]["$from_id"]["member"]="10";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
unlink("data/$from_id.txt");
}
//==============================================================
//panel admin
if($textmassage=="/panel" or $textmassage=="panel" or $textmassage=="مدیریت"){
if(in_array($from_id,$Dev) != false) {
if ($tc == "private") {
sizdahorg('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"🚦ادمین عزیز به پنل مدریت ربات خوش امدید",
         'reply_to_message_id'=>$message_id,
	  'reply_markup'=>json_encode([
    'keyboard'=>[
	  	  	 [
		['text'=>"📍 امار ربات"],['text'=>"📍 ویژه کردن"]                  
		 ],
 	[
	  	['text'=>"📍 ارسال به همه"],['text'=>"📍 فروارد همگانی"]
	  ],
	   	[
	  	['text'=>"📍 افراد انلاین"],['text'=>"📍 مسدود کردن"]
	  ],
	  	   	[
	  	['text'=>"📍 بکاپ از اطلاعات"],['text'=>"📍 حذف ویژه"]
	  ],
	   	[
	  	['text'=>"🔙 برگشت"],['text'=>"📍 ارسال چت فیک"] 
	  ]
   ],
      'resize_keyboard'=>true
   ])
 ]);
}
}
}
elseif($textmassage == "برگشت 🔙") {
sizdahorg('sendmessage',[
'chat_id'=>$chat_id,
'text'=>"🚦 ادمین عزیز به پنل مدریت ربات خوش امدید",
         'reply_to_message_id'=>$message_id,
	  'reply_markup'=>json_encode([
    'keyboard'=>[
	  	  	 [
		['text'=>"📍 امار ربات"],['text'=>"📍 ویژه کردن"]                  
		 ],
 	[
	  	['text'=>"📍 ارسال به همه"],['text'=>"📍 فروارد همگانی"]
	  ],
	   	[
	  	['text'=>"📍 افراد انلاین"],['text'=>"📍 مسدود کردن"]
	  ],
	  	   	[
	  	['text'=>"📍 بکاپ از اطلاعات"],['text'=>"📍 حذف ویژه"]
	  ],
	   	[
	  	['text'=>"🔙 برگشت"],['text'=>"📍 ارسال چت فیک"] 
	  ],
   ],
      'resize_keyboard'=>true
   ])
 ]);
$user["userfild"]["$from_id"]["file"]="none";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
elseif($textmassage=="📍 ارسال چت فیک"){
				sizdahorg('sendmessage',[
		'chat_id'=>$chat_id,
		'text'=>"لطفا عکس را همراه با کپشن [متن زیر عکس] مورد نظر خود ارسال کنید🚀",
   'reply_markup'=>json_encode([
    'keyboard'=>[
	[
	['text'=>"برگشت 🔙"] 
	]
   ],
      'resize_keyboard'=>true
   ])
		]);
$user["userfild"]["$from_id"]["file"]="fakechat";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
		}
elseif ($user["userfild"]["$from_id"]["file"] == 'fakechat') {
if ($textmassage != "برگشت 🔙") {
$user["userfild"]["$from_id"]["file"]="none";
$numbers = $user["userlist"];
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);	
$photo = $message->photo;
$file = $photo[count($photo)-1]->file_id;
$get = sizdahorg('getfile',['file_id'=>$file]);
$patch = $get->result->file_path;
file_put_contents("data/photo.png",file_get_contents("https://api.telegram.org/file/bot$token/$patch"));
         sizdahorg('sendmessage',[
        	'chat_id'=>$chat_id,
        	'text'=>"📍 عکس ذخیره شد در حال ارسال به کابران",
	  'reply_to_message_id'=>$message_id,
 ]);
for($z = 0;$z <= count($numbers)-1;$z++){
     sizdahorg('sendphoto',[
	 'chat_id'=>$numbers[$z],
          'photo'=>new CURLFile("data/photo.png"),        
		  'caption'=>$caption,
		   'reply_markup'=>json_encode([
    'inline_keyboard'=>[
	[
	['text'=>"❤️ شروع چت",'callback_data'=>"chatfake"],['text'=>"🚫 بلاکش کن",'callback_data'=>"blockfake"]
	],
		[
	['text'=>"▶️ بعدی",'callback_data'=>"nextfake"]
	]
	],
        ])
        ]); 
}
}
}
elseif($textmassage=="📍 امار ربات"){
if (in_array($from_id,$Dev)){
$all = count($user["userlist"]);
$chat = count($user["listchat"]);
				sizdahorg('sendmessage',[
		'chat_id'=>$chat_id,
		'text'=>"🤖 امار ربات شما : 
		
📌 تعداد عضو ها : $all

📌 تعداد افراد در انتظار : $chat",
                'hide_keyboard'=>true,
		]);
		}
}
elseif($textmassage=="📍 افراد انلاین"){
if (in_array($from_id,$Dev)){
$chats = count($user["listchat"]);
$chat = $user["listchat"];
for($z = 0;$z <= count($chat)-1;$z++){
$result = $result."[$chat[$z]](tg://user?id=$chat[$z])"."\n";
}
				sizdahorg('sendmessage',[
		'chat_id'=>$chat_id,
		'text'=>"📌 تعداد افراد در انتظار : $chats
		
🔆 لیست افراد :

$result",
		 'parse_mode'=>"MarkDown",
		]);
		}
}
elseif($textmassage=="📍 ویژه کردن"){
if (in_array($from_id,$Dev)){
				sizdahorg('sendmessage',[
		'chat_id'=>$chat_id,
		'text'=>"لطفا یک پیام از کاربر را فوروارد کنید یا ایدی عددی فرد را وارد کنید 🚀",
		]);
$user["userfild"]["$from_id"]["file"]="getvip";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);	
		}
}
elseif ($user["userfild"]["$from_id"]["file"] == 'getvip') {
if ($textmassage != "برگشت 🔙") {
if ($forward_from == true) {
         sizdahorg('sendmessage',[
        	'chat_id'=>$chat_id,
        	'text'=>"کاربر با موفقیت ویژه شد ✔️

🔹ایدی : $forward_from_id
🔸یوزرنیم : @$forward_from_username",
	  'reply_to_message_id'=>$message_id,
 ]);
$user["userfild"]["$forward_from_id"]["vip"]="true";
$user["userfild"]["$forward_from_id"]["member"]="10";
$user["userfild"]["$from_id"]["file"]="none";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
else
{
	         sizdahorg('sendmessage',[
        	'chat_id'=>$chat_id,
        	'text'=>"کاربر با موفقیت ویژه شد ✔️

🔹ایدی : $textmassage",
	  'reply_to_message_id'=>$message_id,
 ]);
$user["userfild"]["$textmassage"]["vip"]="true";
$user["userfild"]["$textmassage"]["member"]="10";
$user["userfild"]["$from_id"]["file"]="none";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
}
}
elseif($textmassage=="📍 حذف ویژه"){
if (in_array($from_id,$Dev)){
				sizdahorg('sendmessage',[
		'chat_id'=>$chat_id,
		'text'=>"لطفا یک پیام از کاربر را فوروارد کنید یا ایدی عددی فرد را وارد کنید 🚀",
		]);
$user["userfild"]["$from_id"]["file"]="remvip";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);	
		}
}
elseif ($user["userfild"]["$from_id"]["file"] == 'remvip') {
if ($textmassage != "برگشت 🔙") {
if ($forward_from == true) {
         sizdahorg('sendmessage',[
        	'chat_id'=>$chat_id,
        	'text'=>"کاربر از حالت ویژه خارج شد ✔️

🔹ایدی : $forward_from_id
🔸یوزرنیم : @$forward_from_username",
	  'reply_to_message_id'=>$message_id,
 ]);
$user["userfild"]["$forward_from_id"]["vip"]="false";
$user["userfild"]["$forward_from_id"]["member"]="0";
$user["userfild"]["$from_id"]["file"]="none";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
else
{
	         sizdahorg('sendmessage',[
        	'chat_id'=>$chat_id,
        	'text'=>"کاربر از حالت ویژه خارج شد ✔️

🔹ایدی : $textmassage",
	  'reply_to_message_id'=>$message_id,
 ]);
$user["userfild"]["$textmassage"]["vip"]="false";
$user["userfild"]["$textmassage"]["member"]="0";
$user["userfild"]["$from_id"]["file"]="none";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
}
}
elseif($textmassage == "📍 مسدود کردن"){
if (in_array($from_id,$Dev)){
				sizdahorg('sendmessage',[
		'chat_id'=>$chat_id,
		'text'=>"لطفا یک پیام از کاربر را فوروارد کنید یا ایدی عددی فرد را وارد کنید 🚀",
   'reply_markup'=>json_encode([
    'keyboard'=>[
	[
	['text'=>"برگشت 🔙"] 
	]
   ],
      'resize_keyboard'=>true
   ])
		]);
$user["userfild"]["$from_id"]["file"]="block";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);	
		}
}
elseif ($user["userfild"]["$from_id"]["file"] == 'block') {
if ($textmassage != "برگشت 🔙") {
if ($forward_from == true) {
         sizdahorg('sendmessage',[
        	'chat_id'=>$chat_id,
        	'text'=>"کابر با موفقیت از ربات مسدود شد ✔️

🔹ایدی : $forward_from_id
🔸یوزرنیم : @$forward_from_username",
	  'reply_to_message_id'=>$message_id,
 ]);
$user["blocklist"][]="$forward_from_id";
$user["userfild"]["$from_id"]["file"]="none";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
}
else
{
	         sizdahorg('sendmessage',[
        	'chat_id'=>$chat_id,
        	'text'=>"کابر با موفقیت از ربات مسدود شد ✔️

🔹ایدی : $textmassage",
	  'reply_to_message_id'=>$message_id,
 ]);
$user["blocklist"][]="$textmassage";
$user["userfild"]["$from_id"]["file"]="none";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);	
}
}
}
elseif ($textmassage == '📍 ارسال به همه' ) {
if (in_array($from_id,$Dev)){
         sizdahorg('sendmessage',[
        	'chat_id'=>$chat_id,
        	'text'=>"لطفا متن خود را ارسال کنید 🚀",
	  'reply_to_message_id'=>$message_id,
	   'reply_markup'=>json_encode([
    'keyboard'=>[
	[
	['text'=>"برگشت 🔙"] 
	]
   ],
      'resize_keyboard'=>true
   ])
 ]);
$user["userfild"]["$from_id"]["file"]="sendtoall";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);	
}
}
elseif ($user["userfild"]["$from_id"]["file"] == 'sendtoall') {
$user["userfild"]["$from_id"]["file"]="none";
$numbers = $user["userlist"];
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);
if ($textmassage != "برگشت 🔙") {
         sizdahorg('sendmessage',[
        	'chat_id'=>$chat_id,
        	'text'=>"پیام با موفقیت ارسال شد ✔️",
	  'reply_to_message_id'=>$message_id,
 ]);
for($z = 0;$z <= count($numbers)-1;$z++){
     sizdahorg('sendmessage',[
          'chat_id'=>$numbers[$z],        
		  'text'=>"$textmassage",
        ]);
}
}
}
elseif ($textmassage == '📍 فروارد همگانی' ) {
if (in_array($from_id,$Dev)){
         sizdahorg('sendmessage',[
        	'chat_id'=>$chat_id,
        	'text'=>"لطفا متن خود را ارسال کنید 🚀",
	  'reply_to_message_id'=>$message_id,
	   'reply_markup'=>json_encode([
    'keyboard'=>[
	[
	['text'=>"برگشت 🔙"] 
	]
   ],
      'resize_keyboard'=>true
   ])
 ]);
$user["userfild"]["$from_id"]["file"]="fortoall";
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);	
}
}
elseif ($user["userfild"]["$from_id"]["file"] == 'fortoall') {
$user["userfild"]["$from_id"]["file"]="none";
$numbers = $user["userlist"];
$user = json_encode($user,true);
file_put_contents("data/user.json",$user);	
if ($textmassage != "برگشت 🔙") {
         sizdahorg('sendmessage',[
        	'chat_id'=>$chat_id,
        	'text'=>"پیام با موفقیت ارسال شد ✔️",
	  'reply_to_message_id'=>$message_id,
 ]);
for($z = 0;$z <= count($numbers)-1;$z++){
Forward($numbers[$z], $chat_id,$message_id);
}
}
}
elseif ($textmassage == "📍 بکاپ از اطلاعات") {
if (in_array($from_id,$Dev)){
         sizdahorg('sendmessage',[
        	'chat_id'=>$chat_id,
        	'text'=>"از اطلاعات کاربران بکاپ گرفته شد 🚀",
	  'reply_to_message_id'=>$message_id,
 ]);
$user = file_get_contents("data/user.json");
file_put_contents("data/backup.json",$user);	
}
}
unlink("error_log");
/*
13HACK-@tmsizdah
*/
?>
