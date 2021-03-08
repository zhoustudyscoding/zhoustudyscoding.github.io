window.onload = function(){
    new Vue({
        el:'#my',
        data:{
            lists:[]
        },
        methods:{
            getList:function(){//拿数据返回给lists
                axios({
                    method:'get',
                    url:'http://localhost:7002/home/page/1/10'
                }).then(function(res){
                    console.log(res)
                }).catch(function(error){

                })
            }
        },
        moounted:function(){//挂载完成钩子函数
            this.getList();
        }
    })
}