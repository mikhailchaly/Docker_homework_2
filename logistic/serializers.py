from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)

        for position in positions:
            StockProduct.objects.create(stock=stock, **position)
        return stock


    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        for position in positions:
            StockProduct.objects.update_or_create(
                stock=stock,
                product=position['product'],
                defaults={'price': position['price'], 'quantity': position['quantity']}
            )

        return stock

        #positions_instance = instance.positions.all()
        # for i in positions_instance:
        #     for j in positions:
        #         if i.product == j['product']:
        #             if 'price' in j:
        #                 i.price = j['price']
        #             if 'quantity' in j:
        #                 i.quantity = j['quantity']
        # if i.product.id != j['product'].id:
        #     StockProduct.objects.create(product=j['product'],
        #                                 price=j['price'],
        #                                 quantity=j['quantity'],
        #                                 stock_id=i.stock_id)

