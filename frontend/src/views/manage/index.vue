<template>
  <div :style="{textAlign:'center'}">
    <h1  >天涯"云团聚"，塔米共此时——答题活动获奖名单</h1>
    <div>
      <input type="text" placeholder="员工编号/部门" />
      <input type="text" placeholder="礼品等级" />
      <button  @click="search">查询</button>
      <button>导出</button>
    </div>
    <hr/>
    <div>
      <table>
        <thead>
          <tr :style="{width:'100%'}">
          <th :style="{width:'100px;'}">工号</th><th>姓名</th><th>部门</th><th>奖品一</th><th>奖品二</th>
          </tr>
        </thead>
        <tbody></tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { getNameList } from '@/api/manage'
export default {
  name: 'manage',
  created() {
     
  },
  methods: { 
    search(){
      getNameList({})
      .then(data=>{console.log('111111111111111',data)})
      .catch(err=>{
        console.log(err)
      })
    }
  },
  beforeRouteEnter(to, from,next) {
    // 在渲染该组件的对应路由被验证前调用
    // 不能获取组件实例 `this` ！
    // 因为当守卫执行时，组件实例还没被创建！
    var person=prompt("请输入获奖名单提取密码","admin");
    if(person == 'admin') {
      next(vm => {
      // 通过 `vm` 访问组件实例
      })
    }
    else {
      next('/manage');
    }
    
  },
}
</script>

<style scoped>
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
