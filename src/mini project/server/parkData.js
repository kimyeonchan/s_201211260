/**
 * http://usejsdoc.org/
 */


var mysql = require('mysql');
var pool = mysql.createPool({
    
      host     : 'localhost',
	  user     : 'root',
	  password : 'root',
	  port     : 3306,
	  database : 'test'
    
    
});

exports.get = (function (req,res){
	var pkData= new Array();
	
	pool.getConnection(function (err, connection){
		var selectquery = "select parking_code, parking_name, addr," +
		"tel, capacity, cur_parking, end_time, rates," +
		"rates_time, add_rate, add_rate_time, day_maximum from parking";
		connection.query(selectquery, function(err, rows){
			if(err){
				console.error('err : ' + err);
			}
			//console.log('rows : ' + JSON.stringify(rows));
			console.log("성공");
			//var jsontext =JSON.stringify(rows);
			//res.write(jsontext ,{'charset':'utf-8'});
			for(var i=0; i<rows.length; i++)
				{
				var item = rows[i];
				pkData[i] = rows[i];
				//console.log(item);
				//var accountObj = JSON.parse(JSON.stringify(pkData[i]));
				}
			res.setHeader('Access-Control-Allow-Origin','*')
			res.send((pkData));

			
			connection.release();
		});
		
		
	});
});


exports.getdetaildata = function(req, res) {
	var code = req.body.code;

	pool.getConnection(function(err, connection) {
		var selectquery = "select * from parking where parking_code='"+ code + "'";
		connection.query(selectquery, function(err, rows) {
			if (err) {
				res.setHeader('Access-Control-Allow-Origin','*')
				console.error('err : ' + err);
				}
			for(var i=0; i<rows.length; i++)
			{
				res.setHeader('Access-Control-Allow-Origin','*')
				res.send(rows[i])
			//var accountObj = JSON.parse(JSON.stringify(pkData[i]));
			}
		});
	});
};