from pbrt.global_objects import SceneElement

class LightSource(SceneElement):

    def __init__(self, Type, Spectrum, From=[0,0,0], Power=[0.0], *args):
        self.Type = Type
        self.Spectrum = Spectrum
        self.From = From
        self.Power = Power
        self.args = list(args)

    def __str__(self):
        # Tranforms Sphere=>sphere, and LightSource=>light_source
        name = self.class_name()

        spectrum_power = "I"

        if type == "distant" or type == "infinte":
            spectrum_power = "L"

        power_str = ''.join(str(e) for e in self.Power)

        out = "{name} \"{type}\" \"{spectrum} {spectrum_power}\" [ {power} ] ".format(name=name,type=self.Type,
                                                                                    spectrum_power=spectrum_power,
                                                                                      power=power_str,
                                                                                    spectrum=self.Spectrum)
        return out

class Attribute(SceneElement):

    def __init__(self, *args):
        self.args = list(args)
        super(Attribute, self).__init__(args)

    def __str__(self):
        return ""