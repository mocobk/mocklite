(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-15e25469"],{"13ba":function(t,e,a){},"7e17":function(t,e,a){},a434:function(t,e,a){"use strict";var o=a("23e7"),r=a("23cb"),n=a("a691"),i=a("50c4"),c=a("7b0b"),s=a("65f0"),l=a("8418"),u=a("1dde"),d=a("ae40"),f=u("splice"),m=d("splice",{ACCESSORS:!0,0:0,1:2}),h=Math.max,p=Math.min,v=9007199254740991,g="Maximum allowed length exceeded";o({target:"Array",proto:!0,forced:!f||!m},{splice:function(t,e){var a,o,u,d,f,m,b=c(this),j=i(b.length),k=r(t,j),D=arguments.length;if(0===D?a=o=0:1===D?(a=0,o=j-k):(a=D-2,o=p(h(n(e),0),j-k)),j+a-o>v)throw TypeError(g);for(u=s(b,o),d=0;d<o;d++)f=k+d,f in b&&l(u,d,b[f]);if(u.length=o,a<o){for(d=k;d<j-o;d++)f=d+o,m=d+a,f in b?b[m]=b[f]:delete b[m];for(d=j;d>j-o+a;d--)delete b[d-1]}else if(a>o)for(d=j-o;d>k;d--)f=d+o-1,m=d+a-1,f in b?b[m]=b[f]:delete b[m];for(d=0;d<a;d++)b[d+k]=arguments[d+2];return b.length=j-o+a,u}})},c8c2:function(t,e,a){"use strict";a.d(e,"g",(function(){return u})),a.d(e,"f",(function(){return d})),a.d(e,"a",(function(){return f})),a.d(e,"k",(function(){return m})),a.d(e,"c",(function(){return h})),a.d(e,"d",(function(){return p})),a.d(e,"h",(function(){return v})),a.d(e,"e",(function(){return g})),a.d(e,"i",(function(){return b})),a.d(e,"b",(function(){return j})),a.d(e,"j",(function(){return k}));var o=a("15fd"),r=(a("d3b7"),a("bc3a")),n=a.n(r),i=a("5c96"),c={baseURL:"http://172.22.23.112:8090",timeout:1e4},s=n.a.create(c);s.interceptors.request.use((function(t){return t}),(function(t){return Promise.reject(t)})),s.interceptors.response.use((function(t){return t.data}),(function(t){if(console.log(t),!t.response)return Object(i["Message"])({message:"连接超时，请检查你的网络！",type:"error",duration:5e3}),Promise.reject(t);var e=t.response.data;return 500===t.response.status&&console.log("something error"),Object(i["Message"])({message:e.message||"出错啦！",type:"error",duration:5e3}),Promise.reject(t)}));(function(){var t=0})();var l=s;function u(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:null;return l({url:"/v1/mock/projects",method:"get",params:t})}function d(t){return l({url:"/v1/mock/projects/".concat(t),method:"get"})}function f(t){return l({url:"/v1/mock/projects",method:"post",data:t})}function m(t,e){return l({url:"/v1/mock/projects/".concat(t),method:"put",data:e})}function h(t){return l({url:"/v1/mock/projects/".concat(t),method:"delete"})}function p(t){return l({url:"/v1/mock/data",method:"get",params:t})}function v(t){return l({url:"/v1/mock/data",method:"post",data:t})}function g(t){return l({url:"/v1/mock/data/".concat(t),method:"get"})}function b(t){var e=t.id,a=Object(o["a"])(t,["id"]);return l({url:"/v1/mock/data/".concat(e),method:"put",data:a})}function j(t){return l({url:"/v1/mock/data/".concat(t),method:"delete"})}function k(t){return l({url:"/v1/mock/test",method:"post",data:t})}},d514:function(t,e,a){"use strict";var o=a("7e17"),r=a.n(o);r.a},f776:function(t,e,a){"use strict";var o=a("13ba"),r=a.n(o);r.a},fa76:function(t,e,a){"use strict";a.r(e);var o=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"view-box"},[a("div",{staticClass:"search"},[a("el-input",{attrs:{placeholder:"请输入关键字",clearable:""},on:{clear:t.searchProjects},nativeOn:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.searchProjects(e)}},model:{value:t.searchWords,callback:function(e){t.searchWords=e},expression:"searchWords"}}),a("el-button",{staticClass:"search-btn",attrs:{icon:"el-icon-search",circle:""},on:{click:t.searchProjects}})],1),a("div",{staticClass:"cards"},[a("el-card",{staticClass:"add",attrs:{shadow:"hover"},nativeOn:{click:function(e){return t.showCreateDialog(e)}}},[a("i",{staticClass:"el-icon-plus"})]),t._l(t.projects,(function(e,o){return a("el-card",{key:o,attrs:{shadow:"hover"},nativeOn:{click:function(a){return t.goMockData(e)}}},[a("div",{staticClass:"header",style:t.getCardStyle(e),attrs:{slot:"header"},slot:"header"},[a("div",{staticClass:"header-text"},[t._v(t._s(e.name))]),a("div",{staticClass:"header-btn"},[a("el-button",{attrs:{icon:"el-icon-edit-outline",size:"mini",circle:""},on:{click:function(a){return a.stopPropagation(),t.showEditDialog(o,e)}}}),a("el-button",{attrs:{icon:"el-icon-delete",size:"mini",circle:""},on:{click:function(a){return a.stopPropagation(),t.deleteProjectData(o,e.id)}}})],1)]),a("div",{staticClass:"description"},[t._v(" "+t._s(e.description||"没有描述")+" ")])])})),t._l(3,(function(t){return a("i",{key:t-4,staticClass:"el-card-fill"})}))],2),a("formDialog",{attrs:{data:t.dialogData||t.defaultDialogData},on:{close:function(e){t.dialogData.visible=!1},success:t.commitSuccess}})],1)},r=[],n=(a("a434"),a("b0c0"),a("5530")),i=a("c8c2"),c=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("el-dialog",{attrs:{title:t.data.title,visible:t.data.visible},on:{"update:visible":function(e){return t.$set(t.data,"visible",e)},close:t.clearValidate}},[a("el-form",{ref:"commitProjectForm",attrs:{model:t.data.item,rules:t.formRules}},[a("el-form-item",{attrs:{label:"项目名称",prop:"name"}},[a("el-input",{model:{value:t.data.item.name,callback:function(e){t.$set(t.data.item,"name",e)},expression:"data.item.name"}})],1),a("el-form-item",{attrs:{label:"项目描述"}},[a("el-input",{attrs:{type:"textarea",rows:4,placeholder:"请输入项目描述"},model:{value:t.data.item.description,callback:function(e){t.$set(t.data.item,"description",e)},expression:"data.item.description"}})],1),a("el-form-item",{staticClass:"card-color-item",attrs:{label:"选择卡片颜色"}},[a("el-color-picker",{attrs:{"show-alpha":"",size:"small",predefine:t.predefineColors},model:{value:t.data.item.color,callback:function(e){t.$set(t.data.item,"color",e)},expression:"data.item.color"}})],1)],1),a("div",{attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:t.closeDialog}},[t._v("取 消")]),a("el-button",{attrs:{type:"primary"},on:{click:t.commitProjectData}},[t._v("确 定")])],1)],1)},s=[],l={name:"FormDialog",props:{data:Object},data:function(){return{predefineColors:["#407434","#a12f2f","#ac5118","#458994","#5b4a42","#9f7d50","#4e1d4c","#005aab","#35363d"],formRules:{name:[{required:!0,message:"请输入项目名称",trigger:"blur"}]}}},methods:{closeDialog:function(){this.$emit("close")},commitProjectData:function(){var t=this;this.$refs["commitProjectForm"].validate((function(e){if(e){var a="创建项目"===t.data.title?i["a"]:function(e){return Object(i["k"])(t.data.item.id,e)};a(t.data.item).then((function(){t.$emit("success"),t.closeDialog()}))}}))},clearValidate:function(){this.$refs["commitProjectForm"].clearValidate()}}},u=l,d=(a("d514"),a("2877")),f=Object(d["a"])(u,c,s,!1,null,"264fb5af",null),m=f.exports,h={name:"Projects",components:{formDialog:m},data:function(){return{searchWords:"",projects:[],defaultDialogData:{title:"创建项目",item:{id:null,name:"",description:"",color:"#35363d"},visible:!1,index:void 0},dialogData:void 0}},created:function(){this.getProjectsData()},methods:{getProjectsData:function(){var t=this,e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:null;Object(i["g"])(e).then((function(e){t.projects=e.data}))},searchProjects:function(){var t=this.searchWords?{search_words:this.searchWords}:null;this.getProjectsData(t)},getCardStyle:function(t){return t.color?{"background-color":t.color}:{}},deleteProjectData:function(t,e){var a=this;this.$confirm("是否确认删除?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then((function(){Object(i["c"])(e).then((function(){a.projects.splice(t,1)})).catch()}))},showCreateDialog:function(){this.dialogData=Object(n["a"])(Object(n["a"])({},this.defaultDialogData),{},{item:Object(n["a"])({},this.defaultDialogData.item),visible:!0})},showEditDialog:function(t,e){this.dialogData={title:"编辑项目",item:Object(n["a"])(Object(n["a"])({},e),{},{color:e.color||this.defaultDialogData.item.color}),visible:!0,index:t}},commitSuccess:function(){var t=this;void 0!==this.dialogData.index?Object(i["f"])(this.dialogData.item.id).then((function(e){t.$set(t.projects,t.dialogData.index,e)})):this.getProjectsData()},goMockData:function(t){this.$router.push({name:"mockData",params:{id:t.id,name:t.name}})}}},p=h,v=(a("f776"),Object(d["a"])(p,o,r,!1,null,"24e46656",null));e["default"]=v.exports}}]);