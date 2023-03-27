#PyTest Decorator
1 -) @pytest.fixture: Bu dekoratör, test fonksiyonlarında kullanılan değişkenleri veya nesneleri tanımlamak için kullanılır. Fixture'lar, testlerin bağımlılıklarını ve bağımsızlıklarını yönetmek için kullanılabilir.

2 -) @pytest.mark.parametrize: Bu dekoratör, aynı testi farklı girdi değerleriyle birkaç kez çalıştırmak için kullanılır. Bu, bir testin farklı durumlarına genel bir yaklaşım sağlar.

3 -) @pytest.mark.skip: Bu dekoratör, belirli bir testin atlanmasını sağlamak için kullanılır. Örneğin, bir testin bir özelliği henüz hazır değilse veya bir hata nedeniyle geçici olarak kullanılamazsa, bu dekoratör kullanılabilir.

4 -) @pytest.mark.xfail: Bu dekoratör, bir testin özellikle hata vermesi veya başarısız olması bekleniyorsa kullanılır. Bu, bir hata veya eksiklik üzerinde çalışırken testlerin çalışmasını sağlar.

5 -) @pytest.mark.timeout: Bu dekoratör, bir testin belirli bir süre içinde tamamlanması gerektiğinde kullanılır. Bu, testlerin aşırı sürelerde çalışmasını önleyebilir.
