from django.db import models

# Create your models here.
class CasosPorCidadePiaui(models.Model):
    """Model definition for CasosPorCidadePiaui."""

    idIBGE = models.IntegerField(verbose_name='IBGE ID', primary_key=True, unique=True)
    name = models.CharField(verbose_name='Name', max_length=80)
    casos = models.IntegerField(verbose_name='Casos')
    obitos = models.IntegerField(verbose_name='Óbitos')

    class Meta:
        """Meta definition for CasosPorCidadePiaui."""

        verbose_name = 'CasosPorCidadePiaui'
        verbose_name_plural = 'CasosPorCidadePiauis'

    def __str__(self):
        """Unicode representation of CasosPorCidadePiaui."""
        return '{}'.format(self.name)
