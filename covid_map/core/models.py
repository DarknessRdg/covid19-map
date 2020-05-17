from django.db import models


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


class UpdateData(models.Model):
    """
    Model to store file name present on folder `/scraps/{name}.py`. Attribute name should be a human readable
    name. The spaces will be replaced for an underscore when loading file.

    An example of implementation:
    # script to update
    - core/
        - scraps/
            - sao_paulo.py  # file names is created lower case and snake case.
                - main()

    # model created
    UpdateData(name='Sao Paulo').save()
    """
    name = models.CharField(help_text='File name to be ran function main()', unique=True, max_length=255)
    active = models.BooleanField(default=True)

    @property
    def file_name(self):
        return self.name.lower().replace(' ', '_')

    def __str__(self):
        return self.name.capitalize()
