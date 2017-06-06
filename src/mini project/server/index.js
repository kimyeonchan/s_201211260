
exports.index = function(req, res){
	//title 변수에 문자열 대입. ejs(jade)파일에서 title 변수 사용할 수 있다.
  res.render('index', { title: 'Express' });
};