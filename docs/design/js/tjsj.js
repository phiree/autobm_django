var vendorids = "119008,118977,119113,119006,119063,118975_118992,118998,119005,119071,119106,119164_118973,119103,119079,119075,119107,118976_118978,119119,119056,119073,119050,118972_119072,119076,119046,119074,119078,119114_119100,119115,119007,119077,118974,118959".split('_');
    var tagCount = vendorids.length;
    var dataArry = new Array();
    var tagIndex = 0;
    var bool = false;
    //显示效果
    function ShowVendor(k) {
        for (var i = 1; i <= 6; i++) {
            if (i == k) {
                document.getElementById("item" + i).style.display = "none";
                document.getElementById("info" + i).style.display = "block";
            } else {
                document.getElementById("item"+i).style.display = "block";
                document.getElementById("info"+i).style.display = "none";
            }
        }
    }
    //加载下一批
    function LoadNewVedor(count) {
        if (tagCount <= 1) {
            document.getElementById("HNewVendor").innerHTML = "新店大酬宾";
        } else {
            document.getElementById("HNewVendor").innerHTML = "<strong>新店大酬宾</strong><a  class=\"o\" href=\"javascript:void(0)\" onclick=\"ChangeVendor(" + (count >= tagCount-1 ? 0 : count+1) + ");\">换一批</a>";
        }
        var item = "<div id=\"item{0}\" style=\"display:{1};\"><div class=\"index_c_r_3_1\"><span><strong>{3}</strong>&nbsp;{4}折</span>";
        item += "<strong><dfn class=\"rmb\">&yen;</dfn>{5}起</strong></div><div class=\"index_c_r_3_2\"><span>[{6}]</span>";
        item += "{7}</div></div>";		

        var info = "<div id=\"info{0}\" style=\"display:{5};\"><div><a href=\"/{6}/\" target=\"_blank\"><img src=\"{1}\" /></a></div><div class=\"tj_1\"><a href=\"/{6}/\" target=\"_blank\" >{2}</a>[{3}]";
        info += "</div><div class=\"tj_2\">特惠服务：</div>";

        var ddcontent = "<div class=\"tj_3 b\"><span><a href=\"{0}\" target=\"_blank\">{1}</a></span><a href=\"{0}\" target=\"_blank\" class=\"r\"><dfn class=\"rmb\">&yen;</dfn>{2}起</a>{3}</div></div>";		
		
        var dcontent = "";
        var strHtml = "";
        SendRequest("/Handler/Service.ashx", "post", "action=getNewVendoeService&cityid=440100&vendorIds=" + count + "&temp=" + new Date().getTime(), function (msg) {
            if (msg != "") {
                if (msg == "0") {
                        
                } else {
                    var serJson = "";
                    try {
                        eval("serJson=" + msg);
                        for (var i = 0; i < serJson.length; i++) {
                            strHtml += "<li onmouseover=\"ShowVendor(" + (i + 1) + ");\">";
                            strHtml += item.replace(/\{0}/g, i + 1).replace(/\{1}/g, i == 0 ? "none" : "block").replace(/\{2}/g, (serJson[i].MinFilm ? "/s_f/" : "/s/") + serJson[i].ServiceId + "/?itemid=" + serJson[i].ItemId).replace(/\{3}/g, serJson[i].MinName).replace(/\{4}/g, serJson[i].MinDiscount).replace(/\{5}/g, serJson[i].MinPrice).replace(/\{6}/g, serJson[i].CountyName).replace(/\{7}/g, serJson[i].VendorName);

                            if (serJson[i].ListVendorService != "") {
                                dcontent = "";

                                for (var j = 0; j < serJson[i].ListVendorService.length; j++) {
                                    dcontent += ddcontent.replace(/\{0}/g, (serJson[i].ListVendorService[j].IsFilm ? "/s_f/" : "/s/") + serJson[i].ListVendorService[j].ServiceId + "/?itemid=" + serJson[i].ListVendorService[j].Id).replace(/\{1}/g, serJson[i].ListVendorService[j].Name).replace(/\{2}/g, serJson[i].ListVendorService[j].Price).replace(/\{3}/g, j == 0 ? "<div class=\"clearfloat\"></div>" : " ");
                                }
                            }
                            strHtml += info.replace(/\{0}/g, i + 1).replace(/\{1}/g, (serJson[i].Img == "" ? "http://x.autoimg.cn/y/site/img/nophoto180.gif" : getStaticImage("http://y{0}.autoimg.cn/vendor/180/" + serJson[i].Img))).replace(/\{2}/g, serJson[i].VendorName).replace(/\{3}/g, serJson[i].CountyName).replace(/\{4}/g, dcontent).replace(/\{5}/g, i == 0 ? "block" : "none").replace(/\{6}/g, serJson[i].VendorId);
                            strHtml += "</li>";
                        }
                        document.getElementById("ulNewVendor").innerHTML = strHtml;
                        dataArry[tagIndex] = strHtml; //保存数据到数组中
                        tagIndex++;
                    } catch(e) {

                    }
                }
            }
        });
    }

    //点击事件
    function ChangeVendor(num) {
        document.getElementById("ulNewVendor").innerHTML = "<div class=\"loading\"><img src=\"../images/loading2.gif\"></div>";
            
        if (tagIndex == tagCount) {//如果数组没存满则继续读取数据库数据
            if (bool) {
                document.getElementById("HNewVendor").innerHTML = "<a href=\"javascript:void(0)\" onclick=\"ChangeVendor(" + (num + 1 >= dataArry.length - 1?0:num+1) + ");\">换一批</a>新店大酬宾";
                document.getElementById("ulNewVendor").innerHTML = dataArry[num + 1];
                if (num + 1 == dataArry.length - 1) {
                    bool = false; //索引回归到初始位置
                }
            } else {
                document.getElementById("ulNewVendor").innerHTML = dataArry[num];
                bool = true;//数组从零开始
            }
        } else {
            LoadNewVedor(num);
        }

    }

    function InitLoad() {
        dataArry[tagIndex] = document.getElementById("ulNewVendor").innerHTML;
        tagIndex++;
    }    
    //计算图片路径
    function getStaticImage(path) {
        var str = path.toLowerCase().substring(path.lastIndexOf('/') + 1);
        var b = 0, i = 0;
        while ((i += 4) < str.length) { b ^= str.charCodeAt(i); }
        b %= 2;
        return path.replace(/\{0}/g, b);
    }