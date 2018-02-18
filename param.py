import math


class Param:
    big_y_air = None
    big_y_surface = None
    ft_result_air = None
    ft_result_surface = None

    def __init__(self, sc_dist, const_u_air, const_u_surface, log_scale_dist, list_slope_u_air, list_slope_u_surface, limits, const_y):
        self.sc_dist = sc_dist
        self.u_air = const_u_air[0] + const_u_air[1] * log_scale_dist
        self.u_surface = const_u_surface[0] + const_u_surface[1] * log_scale_dist
        self.list_slope_u = [
            list_slope_u_air,
            list_slope_u_surface
        ]
        self.limits = limits
        self.const_y = const_y

    def get_fn_u_pow(self, slope, power, type_idx):
        if type_idx == 0:
            return slope * math.pow(self.u_air, power)
        else:
            return slope * math.pow(self.u_surface, power)

    def get_list_fn_u(self, slopes, type_idx):
        storage = []

        for idx, item in enumerate(slopes):
            storage.append(self.get_fn_u_pow(item, idx + 1, type_idx))
        return storage

    def get_y(self):
        # evaluate result for both air and surface cases
        # print('self.list_slope_u', self.list_slope_u)
        for idx, slopes in enumerate(self.list_slope_u):
            list_fn = self.get_list_fn_u(slopes, idx)
            # print('slopes', idx, slopes)
            y = self.const_y[idx] + sum(list_fn)
            # print('idx', idx, 'y', y)
            if idx == 0:
                self.big_y_air = y
            else:
                self.big_y_surface = y
        return [
            self.big_y_air,
            self.big_y_surface
        ]

    def get_ft_result(self):
        ys = self.get_y()
        limits = self.limits
        print('limits', limits)
        sc_dist = self.sc_dist

        for idx, y in enumerate(ys):
            limit = limits[idx]
            print('limit', limit, idx)
            if sc_dist < limit['lower_limit'] or sc_dist > limit['upper_limit']:
                if idx == 0:
                    self.ft_result_air = 0
                else:
                    self.ft_result_surface = 0
            else:
                if idx == 0:
                    self.ft_result_air = y
                else:
                    self.ft_result_surface = y
        return [
            self.ft_result_air,
            self.ft_result_surface
        ]
