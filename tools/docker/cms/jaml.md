1.CAS 原理

1.1.CAS 简介
单点登录（Single Sign-On , 简称SSO）是在多个应用系统中，用户只需要登录一次就可以访问所有相互信任的应用系统，服务于企业业务整合的解决方案。CAS是为Web应用系统提供一种企业级的开源的单点登录解决方案。
                
      














     

                                                            CAS 结构图
  从上图可知，CAS体系结构主要包含两部分组成：CAS Server以及CAS Client。














1)CAS Server : 主要负责对用户认证并授权用户对各应用系统的访问。用户认证是用户通过浏览器调用CAS Server而授权访问时是CAS Client（内嵌于受保护的应用中）调用CAS Server，用户认证与授权具体流程在单点登录中将详细阐述。CAS Server 内部主要由Authentication模块和Ticket模块组成。Authentication模块用于订制用户验证的方式，如基于数据库、LDAP、OAuth等，模块只提供认证接口，用户可以按需自定义认证具体实现。Ticket模块主要用于存储验证凭证信息，如Service Ticket。
2)CAS Client : 负责处理对受保护资源的访问请求。需要对请求方进行身份认证时，重定向到CAS Server进行认证。它集成于应用中，并可通过授权协议（如CAS, SAML, OAuth）与CAS Server 通信。
名词解释:
TGT － Ticket Granting Ticket，用户身份认证凭证票据。
ST － Service Ticket，服务许可凭证票据。
TGC － Ticket Granting Cookie，存放用户身份认证凭证票据的cookie。
SSO Session － 由CAS服务器产生，记录经过认证用户的信息，它对应的cookie发放到用户使用的浏览器中,而不是在CAS Client 中。
Application Session － 由各应用服务器为经过CAS 认证授权的用户产生的本应用专门的信息记录容器，它对应的cookie发放到用户使用的浏览器中。

需要注意SSO Session与Application Session 并无直接关联。SSO Session 销毁不会直接导致Application Session销毁，Application Session 销毁也不会直接导致SSO Session销毁。但如果CAS配置单点登出（Single Logout ,SLO)情况下，两者销毁具有同步性，下文讲解单点登出时将详细介绍。























1.2.单点登录原理
CAS被设计为一个独立的Web应用，必须运行在支持SSL的web服务器之上，以保证Ticket Granting Cookie和Service Ticket 安全传递。应用程序可以通过三个URL路径来使用CAS，分别是登录URL（login URL），校验Ticket URL（validation URL）和登出URL（logout URL）。 CAS Client 与受保护的客户端应用集成在一起，以 Filter 方式保护 Web 应用。当用户首次访问受保护应用时候，具体流程：
1)用户访问 protect web app1 时，protect web app1（CAS Client）判断用户没有登录(http请求中没有App Session下放的cookie或请求未携带ticket 参数)，将请求重定向到CAS 服务器登录界面。需要注意的是重定向CAS url中传递的service参数,其值是要访问的受保护应用的目的资源地址。

2)用户在CAS 登录界面输入用户名密码并CAS 验证通过后，CAS Server 创建用户对应的SSO Session，下放Ticket Granting Cookie到浏览器。客户端浏览器此后再次访问CAS Server 时，携带Ticket Granting Cookie，CAS Server 判断是否存在Cooki对应的Session，如果存在将无需认证。下放Cookie的同时，CAS Server 将请求重定向请求到第1步传递过来的service 地址，同时在地址中传递Service Ticket。

3)浏览器保存Ticket Granting Cookie，同时请求service 地址，即 protect web app1 。protect web app1 判断请求中携带有ticket 参数，app 1 将调用CAS的校验Ticket URL并在URL地址中传递service地址参数和ticket 参数。CAS Server 校验ticket 合法，将建立service地址和ticket 之间的关联，这在之后的单点登出中将起到重要作用。app 1得到CAS Server 验证成功返回信息后，将新建 Application Session 并设置Session 对应的Cookie到浏览器。此后，浏览器访问app1 时，请求中携带此Cookie，app1将无需验证此用户。

详细流程说明，如下图。    





























以上说明了web app1首次登陆流程，当用户在同一个浏览器访问web app2时流程如下：
1)用户访问 web app2 ,web app2 检测到请求中没有app2的Application Session 或ticket，重定向请求到CAS Server并在请求中携带service url地址。因为在app1 中，浏览器中存储有CAS Server 域名相应的cookie，再次请求CAS Server 时，请求携带此cookie 到服务器，CAS Server 验证存在cookie 对应Session,重定向请求到传递过来的service 地址并传递Service Ticket。
    
2)web app2 再次收到请求后，请求参数中存在ticket参数，将去CAS Server 验证ticket合法性。
app2受到验证成功信息后，为此用户创建app2的Application Session并下发相应cookie到浏览     
器。用户再次访问 app2,app2能根据请求中cookie 判定用户合法性。

具体流程如下图。












用户在同一浏览器访问其他受CAS Server 保护的web app 时流程相似。

1.3.单点登出原理
用户在同一浏览器访问多个受 CAS 保护的站点，验证和授权通过后 CAS Server 建立此用户的SSO Session，同时各个站点为用户建立各自Application Session。一个站点Application Session的销毁，不会导致SSO Session的销毁，也不会导致和此站点利用同一SSO Session验证的其他站点的Application Session的销毁。所谓单点登出就是SSO Session销毁会导致利用此SSO Session验证用户的Application Sessions的销毁。
用户在protected web app1界面登出，集成于app1内的CAS Client拦截到该请求然后将请求重定向到CAS Server。浏览器携带CAS Server发放的Ticket Granting Cookie请求CAS Server。
CAS Server 收到logout请求，销毁Ticket Granting Cookie对应的Session。同时，最重要的是回调通知和此Session关联的各web app的service url 通知各web app 销毁各自Application Session,完成单点登出。
流程如下图。







CAS Server 通过HTTP POST 请求发送登出消息到各个web app，消息格式：
<samlp:LogoutRequest
    xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    ID="[RANDOM ID]"
    Version="2.0"
    IssueInstant="[CURRENT DATE/TIME]">
    <saml:NameID>@NOT_USED@</saml:NameID>
    <samlp:SessionIndex>[SESSION IDENTIFIER]</samlp:SessionIndex>
</samlp:LogoutRequest>
 其中session identifier是CAS Server 提供给应用服务器的Service Ticket，这个Ticket 用于在web app server中查找其相对应的Application Session。Service Ticket和Application Session之间的映射关系是由CAS Client 维护，并且在Ticket向CAS Server 验证成功后建立映射，这种映射关系在单点登出时候销毁。
2.CAS Server部署
前文提到CAS 可以自定义用户验证的Handler ，只需实现AuthenticationHandler接口并配置为默认的密码验证Handler。我们单点登陆系统主要由CAS,JumpServer,Gitlab,Jenkins,Zabbix系统组成，其中所有的用户信息在 JumpServer中创建、修改、删除。同时，CAS 和JumpServer 共用同一个用户表，因此，自定义AuthenticationHandler用户密码的解密方式和JumpServer加密方式需相互对应。具体代码见：
cas-4.1.4/cas-server-support-jdbc/src/main/java/org/jasig/cas/adaptors/jdbc/MD5JdbcPasswordAuthenticationHandler.java
CAS Server 部署主要分为两个步骤：1修改CAS配置文件编译打包war 包；2 在tomcat中启动https 支持。
1)CAS 默认认证Handler 为AcceptUsersAuthenticationHandler，因此要替换为自定义实现的MD5JdbcPasswordAuthenticationHandler.java.













<!-- #注释掉默认的Handler
<bean id="primaryAuthenticationHandler"
          class="org.jasig.cas.authentication.AcceptUsersAuthenticationHandler">
        <property name="users">
            <map>
                <entry key="casuser" value="Mellon"/>
            </map>
        </property>
    </bean>
-->  
#添加自定义实现Handler
<beanid="primaryAuthenticationHandler"  
              class="org.jasig.cas.adaptors.jdbc.MD5JdbcPasswordAuthenticationHandler">
              <property name="dataSource" ref="dataSource" />
         <property name="sql" value="select password from juser_user where lower(username) = lower(?)" />
</bean>
<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
	<property name="driverClassName">
                    <value>com.mysql.jdbc.Driver</value></property>
	    <property name="url">
                         <value>jdbc:mysql://localhost:3306/jumpserver</value>
	    </property>
	    <property name="username">
                         <value>xxx</value>
	    </property>
	    <property name="password"> 
                        <value>xxx</value> 
	    </property>
</bean>
文件在cas-4.1.4/cas-server-webapp/src/main/webapp/WEB-INF/deployerConfigContext.xml 中。













另外，在cas-4.1.4/cas-server-webapp/pom.xml文件中要引入mysql jdbc java lib。
<dependency>
	<groupId>org.jasig.cas</groupId>
	<artifactId>cas-server-support-jdbc</artifactId>
	<version>${project.version}</version>
</dependency>
<dependency>
	<groupId>commons-dbcp</groupId>
	<artifactId>commons-dbcp</artifactId>
	<version>1.4</version>
	<scope>runtime</scope>
</dependency>
<dependency>
	<groupId>mysql</groupId>
	<artifactId>mysql-connector-java</artifactId>
	<version>5.1.6</version>
	<scope>runtime</scope>
</dependency>

最重要：配置CAS用启用HTTPS。CAS 默认是启用了HTTPS,如果关闭HTTPS,CAS单点登陆功能将不能用，因为CAS 需要HTTPS来安全地传递Ticket Granting Cookie。
<bean id="ticketGrantingTicketCookieGenerator"   
               class="org.jasig.cas.web.support.CookieRetrievingCookieGenerator"
          c:casCookieValueManager-ref="cookieValueManager"
          p:cookieSecure="true"  #必须为 true
          p:cookieMaxAge="-1"
          p:cookieName="TGC"
          p:cookiePath=""/>
配置在cas-4.1.4/cas-server-webapp/src/main/webapp/WEB-INF/spring-configuration/ticketGrantingTicketCookieGenerator.xml 文件中













<bean id="warnCookieGenerator" class="org.jasig.cas.web.support.CookieRetrievingCookieGenerator"
          p:cookieSecure="true" #必须为 true
          p:cookieMaxAge="-1"
          p:cookieName="CASPRIVACY"
          p:cookiePath=""/>
配置在cas-4.1.4/cas-server-webapp/src/main/webapp/WEB-INF/spring-configuration/warnCookieGenerator.xml文件中
2)tomcat中启动https 支持，需要制作https 证书并配置tomcat开启https。
首先，为名为cas的证书创建keystore文件并存放在当前目录下。
keytool -genkey -alias cas -keyalg RSA -storepass changeit -keystore .keystore -validity 3600
然后，导出cas.cer 证书到当前目录下。
keytool -export -trustcacerts -alias cas -file tomcat.cer -keystore .keystore -storepass changeit
其次，将证书导入到tomcat 所在主机的JDK证书信任库。
keytool -import -trustcacerts -alias cas -file cas.cer -keystore "$JAVA_HOME/jre7/lib/security/cacerts" -storepass changeit
最后，配置tomcat server.xml文件(服务器需要https登陆验证)
<Connector port="8443" protocol="org.apache.coyote.http11.Http11NioProtocol"
               maxThreads="150" SSLEnabled="true" scheme="https" secure="true"
               clientAuth="false" sslProtocol="TLS" URIEncoding="UTF-8" 
               keystoreFile="path to .keystore file" 
               keystorePass="password of .keystore file" 
               keyAlias="cas"  />




	













3.JumpServer 
JumpServer 支持单点登陆需把原本登陆和登出url 转移到CAS python语言客户端python-cas-ng中来，配置修改于jaml/jumpserver/urls.py。
    url(r'^$', 'index', name='index'),
    # url(r'^api/user/$', 'api_user'),
url(r'^skin_config/$', 'skin_config', name='skin_config'),
＃  url(r'^login/$', 'Login', name='login'),　注释掉原本的登陆认证界面
＃　url(r'^logout/$', 'Logout', name='logout'),
    url(r'^exec_cmd/$', 'exec_cmd', name='exec_cmd'),
    url(r'^file/upload/$', 'upload', name='file_upload'),
    url(r'^file/download/$', 'download', name='file_download'),
    url(r'^setting', 'setting', name='setting'),
    url(r'^terminal/$', 'web_terminal', name='terminal'),
    url(r'^juser/', include('juser.urls')),
    url(r'^jasset/', include('jasset.urls')),
    url(r'^jlog/', include('jlog.urls')),
    url(r'^jperm/', include('jperm.urls')),
    url(r'^login/$', django_cas_ng.views.login, name='login'),#添加用户认证到CAS 
　　url(r'^logout/$', django_cas_ng.views.logout, name='logout'),#添加用户登出到CAS处理 
　　url(r'^callback/$', django_cas_ng.views.callback, name='cas_ng_proxy_callback'),
JumpServer 部署之前需要按序安装python-cas,python-cas-ng。但python-cas和python-cas-ng源码中对单点登出功能支持本身存在bug,同时用户应该存在角色的区别而python-cas-ng源码中没有体现经过CAS认证的用户拥有角色，因此需要修改两者源代码。

















python-cas源码修改:
class CASClientBase(object):
      ........
　　　"""添加LogoutRequest解析函数"""
    def get_saml_slos(self, logout_request):　
　　　　"""returns saml logout ticket info"""
　　　　from lxml import etree
　　　　try:
	root = etree.fromstring(logout_request)
	return root.xpath(
	        "//samlp:SessionIndex",
	        namespaces={'samlp': "urn:oasis:names:tc:SAML:2.0:protocol"})
　　　　except etree.XMLSyntaxError:
	pass
源码见http://112.74.52.16:8000/nathan/python-cas.git。
python-cas-ng源码修改：
def login(request, next_page=None, required=False):
    if request.method == 'POST' and request.POST.get('logoutRequest'): #添加单点登出处理
        clean_sessions(get_cas_client(), request)
        return HttpResponse("{0}\n".format(_('ok')), content_type="text/plain")
　　...
        if user is not None:
            auth_login(request, user)
            if user.role == 'SU':　＃用户进过CAS 认证后添加角色属性
                request.session['role_id'] = 2
            elif user.role == 'GA':
                request.session['role_id'] = 1
            else:          request.session['role_id'] = 0
源码见http://112.74.52.16:8000/nathan/django-cas-ng.git
需要注意：安装python-cas和django-cas-ng需要从源码安装，而不是通过pip直接安装。












4.Gitlab 
Gitlab安装包中已有ＣAS客户端支持，因此只需在配置文件中修改认证方式就可改变原有认证方式到CAS,修改如下：
gitlab_rails['omniauth_enabled'] = true　＃开启omniauth
gitlab_rails['omniauth_allow_single_sign_on'] = true　＃开启单点登陆
gitlab_rails['omniauth_auto_sign_in_with_provider'] = 'cas3'　＃开启默认cas 用户认证方式
gitlab_rails['omniauth_block_auto_created_users'] = true　
gitlab_rails['omniauth_providers'] = [
   {
     "name" => "cas3",
     "label" => "cas3",
     "args" => { 　＃CAS Server 配置
         "url"=> 'https://ywcas.bigbigcloud.cn:8443',
         "login_url"=> '/cas/login',
         "disable_ssl_verification" => true,
         "service_validate_url"=> '/cas/serviceValidate',
         "logout_url"=> '/cas/logout',
      }
   }
 ]
配置文件在/etc/gitlab/gitlab.rb。修改配置后，需要执行以下命令：

gitlab-ctl reconfigure
gitlab-ctl restart

另外，编辑gitlab/embedded/service/gitlab-rails/app/views/layouts/header/_default.html.haml
将 destroy_user_session_path 替换为 gitlab在CAS Server logout url，以支持单点登出。	

