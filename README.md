# Bootcamp-Proje
Global AI Hub Bootcamp Projesi

Giriş

Bu proje, Intel Image Classification Dataset kullanılarak doğal görüntülerin (bina, orman, deniz, dağ, sokak ve çöl) sınıflandırılması amacıyla gerçekleştirilmiştir.

Çalışma kapsamında:

Sıfırdan CNN mimarisi oluşturulmuş,
Transfer Learning yöntemiyle MobileNetV2 modeli kullanılmış,
Farklı optimizasyon algoritmaları (Adam, RMSprop, SGD) test edilerek performansları karşılaştırılmıştır.
Tüm adımlar, veri hazırlamadan model değerlendirmeye kadar detaylı olarak anlatılmış ve görselleştirilmiştir.

Kullanılan Yöntemler

Veri Hazırlama: Görseller normalize edilerek modele uygun hale getirildi. Etiketler one-hot encode edildi ve veri artırma (augmentation) teknikleri uygulandı.

Model 1 - Custom CNN:
Katman sayısı artırılmış, Batch Normalization ve Dropout gibi düzenleme teknikleriyle optimize edilmiş özel bir CNN modeli geliştirildi.

Model 2 - Transfer Learning:
MobileNetV2 modeli kullanıldı. Üst katmanlar değiştirilerek yalnızca son katmanlar yeniden eğitildi.

Optimizasyon Karşılaştırması:
Adam, RMSprop ve SGD algoritmaları test edildi. En iyi performans Adam ile elde edildi.

📈 Elde Edilen Sonuçlar
Model	Test Doğruluğu
Custom CNN	0.9053
MobileNetV2 (Transfer)	0.9070
En İyi Optimizatör (RMSprop)	0.8497

Transfer Learning, sıfırdan eğitilen modele göre az da olsa daha yüksek doğruluk sağlamıştır.
RMSprop optimizasyon algoritması, diğer optimizyonlara göre hem öğrenme hızı hem doğruluk açısından en verimli sonuçları vermiştir.
Model karşılaştırmaları grafiklerle görselleştirilmiş, doğru/yanlış tahmin örnekleri gösterilmiştir.
Eğitim süreci boyunca overfitting riski erken durdurma ve veri artırma ile minimize edilmiştir.

Ekler

Proje ilerleyen aşamalarda aşağıdaki yönlerde genişletilmeye uygundur:
Streamlit ile Arayüz Geliştirme: Kullanıcıların resim yükleyip sınıf tahmini alabileceği basit bir arayüz.
Model Deploy (End-to-End): Trained modelin bir API olarak deploy edilmesi (örneğin FastAPI veya Flask ile).
Gerçek Zamanlı Görüntü Sınıflandırma: Webcam üzerinden canlı görüntü alınıp sınıflandırılması.

onuç ve Gelecek Çalışmalar

Bu proje, temel görüntü sınıflandırma tekniklerini hem sıfırdan hem de hazır modellerle deneyimlemek adına etkili bir uygulama olmuştur.

Gelecekte Eklenebilecekler

Modelin karmaşıklığını azaltmak için model boyutu ve hız optimizasyonu yapılabilir.
Veri seti büyütülerek veya farklı veri kaynakları eklenerek genelleme yeteneği artırılabilir.
Daha ileri seviye mimariler (EfficientNet, Vision Transformer) denenebilir.
Kullanıcı arayüzü ve canlı demo entegrasyonu ile proje ürünleşmeye uygun hale getirilebilir.

LİNK
https://www.kaggle.com/code/mhseyinatalan/derin-renme-uygulamas-bootcamp
