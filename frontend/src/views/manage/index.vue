<template>
  <div :style="{textAlign:'center'}">
    <h1>天涯"云团聚"，塔米共此时——答题活动获奖名单</h1>
    <div>
      <input type="text" placeholder="员工编号/姓名" v-model="searchKey" />
      <select  v-model="selected_gift">
        <!-- <option :value="-1">--请选择奖品--</option> -->
        <option v-for="(gift,index) in gifts" :key="index" :value="index">{{gift}}</option>
    
      </select>
      <button  @click="search">查询</button>
      <button @click="exportExcel">导出</button>
      <button class="logout" v-show="showLogout" @click="logout">[退出]</button>
    </div>
    <hr/>
    <div>
      <table>
        <thead>
          <tr >
          <th >工号</th><th>姓名</th><th>部门</th><th>奖品一</th><th>奖品二</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item,index in members" :key="index">
            <td>{{item.username}}</td>
            <td>{{item.nick_name}}</td>
            <td>{{item.dept_name}}</td>
            <td>{{item.first_prize_level >0 ? gifts[item.first_prize_level]: '--'}}</td>
            <td>{{item.second_prize_level >0 ? gifts[item.second_prize_level]: '--'}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { getNameList,getExcel } from '@/api/manage'
import { mapGetters } from "vuex";
import { gotopPage } from "@/utils/index";
export default {
  name: 'manage',
  data() {
    return {
      members: [],
      showLogout:false,
      selected_gift: 0,
      searchKey:"",
      gifts: ['--请选择奖品--','户外座椅-灰','阿维塔定制保温杯','城市画展系列T恤衫-XL',
     '户外超声波防潮野餐地垫-灰','户外折叠整理箱-灰','AVATR环保束口包','AVATR精品帆布包（含定制徽章）','杜邦电脑包','E值-66'],
      // gifts:[
      //   {level:1,name:'户外座椅-灰'},
      //   {level:2,name:'阿维塔定制保温杯'},
      //   {level:3,name:'城市画展系列T恤衫-XL'},
      //   {level:4,name:'户外超声波防潮野餐地垫-灰'},
      //   {level:5,name:'户外折叠整理箱-灰'},
      //   {level:6,name:'AVATR环保束口包'},
      //   {level:7,name:'AVATR精品帆布包（含定制徽章）'},
      //   {level:8,name:'杜邦电脑包'},
      //   {level:9,name:'E值-66'},
      // ]
    };
  },
  created() {
     
  },
  computed: {
    ...mapGetters(["token","roles"]),
  },
  methods: { 
    search(){
      getNameList({searchKey: this.searchKey, gift: this.selected_gift})
      .then(data=>{
        //console.log('lucky boys:',data)
        this.members=data.data;
      })
      .catch(err=>{
        console.log(err)
      })
    },
    exportExcel(){
      getExcel({searchKey: this.searchKey, gift: this.selected_gift})
      .then(res=>{
          //console.log('lucky boys:',res)
          //const content = res.data;
          //const blob = new Blob([content]);
          let blob = new Blob([res.data], {
          type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=utf-8',
        });
          const fileName = "塔迷2022年度中秋抽奖数据.xls";
          if ("download" in document.createElement("a")) { // 非IE下载
            const elink = document.createElement("a");
            elink.download = fileName;
            elink.style.display = "none";
            //console.log('xxxxxx',blob);
            elink.href = URL.createObjectURL(blob);
            document.body.appendChild(elink);
            elink.click();
            URL.revokeObjectURL(elink.href); // 释放URL 对象
            document.body.removeChild(elink);
          } else { // IE10+下载
            navigator.msSaveBlob(blob, fileName);
          }
      })
      .catch(err=>{
        console.log(err)
      })
    },
    logout() {
      this.$store.dispatch('user/logout')
      .then(() => {
        console.log(11111);
        this.showLogout = false;
        gotopPage('/home');
      })
      .catch(err=>{
        console.log(err);1111
        gotopPage('/home');
      })
    },
    async adminConfirm(times=0){
      var msg = "请输入获奖名单提取密码:";
      if(times){
        msg = "验证错误，请重新输入！"
      }
      try {
          console.log("AAAAA",this.roles);
          await  this.$store.dispatch('user/getInfo');
          console.log("BBBBB",this.roles[0]);
          if(this.roles[0] == 'admin') {
            this.showLogout = true;
            return;
          }
      }catch(err){
          
      }
      if(times < 3) {
        var person=prompt(msg,"");
        if(person && person == '123456Aa') {
          try {
            await this.$store.dispatch('user/loginAdmin', {username: 'admin', password: 'admin'});
            this.showLogout = true;
          }
          catch(err) {
            console.log(err);
            await this.adminConfirm(times+1)
          }
        }
        else{
          await this.adminConfirm(times+1)
        }
      }
      else {
        alert('密码没记住，问下管理员呢？');
      }
    }
  },
  mounted() {
    
    this.adminConfirm(0)
    .then(()=>{
      console.log(`the component is now mounted.${this.token}`)
    })
    .catch(err=>{
      this.$router.replace({ path: '/home' })
    })
  },
  // beforeRouteEnter(to, from,next) {
  //   // 在渲染该组件的对应路由被验证前调用
  //   // 不能获取组件实例 `this` ！
  //   // 因为当守卫执行时，组件实例还没被创建！
  //   var person=prompt("请输入获奖名单提取密码","admin");
  //   if(person == 'admin') {
  //     next(vm => {
  //     // 通过 `vm` 访问组件实例
  //     this.$store.dispatch('user/login', {username: 'admin', password: 'admin'}).then(() => {
  //           this.$router.push({ name: 'manage' })
  //         }).catch(() => {

  //         })
  //     })
  //   }
  //   else {
  //     next('/manage');
  //   }
    
  // },
}
</script>

<style scoped>

input, textarea, button, select, a {
  border: solid 1px;
  height:29px;
  width: auto;
  line-height:2;
  margin-right: 10px;
}

button {
  width: 80px;
  cursor:pointer;
}
.logout {
    float: right;
    margin-right: 15px;
  }
h1 {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 20px;
}
table {

width: 700px;

padding: 0;

margin: auto;

}

caption {

padding: 0 0 5px 0;

width: 700px;

font: italic 11px "Trebuchet MS", Verdana, Arial, Helvetica, sans-serif;

text-align: right;

}

th {

font: bold 11px "Trebuchet MS", Verdana, Arial, Helvetica, sans-serif;

color: #4f6b72;

border-right: 1px solid #C1DAD7;

border-bottom: 1px solid #C1DAD7;

border-top: 1px solid #C1DAD7;

letter-spacing: 2px;

text-transform: uppercase;

text-align: left;

padding: 6px 6px 6px 12px;

background: #CAE8EA no-repeat;

}

th.nobg {

border-top: 0;

border-left: 0;

border-right: 1px solid #C1DAD7;

background: none;

}

td {

border-right: 1px solid #C1DAD7;

border-bottom: 1px solid #C1DAD7;

background: #fff;

font-size:11px;

padding: 6px 6px 6px 12px;

color: #4f6b72;

}

td.alt {

background: #F5FAFA;

color: #797268;

}

th.spec {

border-left: 1px solid #C1DAD7;

border-top: 0;

background: #fff no-repeat;

font: bold 10px "Trebuchet MS", Verdana, Arial, Helvetica, sans-serif;

}

th.specalt {

border-left: 1px solid #C1DAD7;

border-top: 0;

background: #f5fafa no-repeat;

font: bold 10px "Trebuchet MS", Verdana, Arial, Helvetica, sans-serif;

color: #797268;

}
</style>
