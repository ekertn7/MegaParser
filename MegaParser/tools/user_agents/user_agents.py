from typing import Iterable
from fake_useragent import UserAgent

__all__ = [
    'UserAgentBrowsers',
    'UserAgentOperatingSystems',
    'UserAgentPlatforms',
    'generate_user_agent'
]


class UserAgentBrowsers:
    CHROME = 'chrome'
    EDGE = 'edge'
    FIREFOX = 'firefox'
    SAFARI = 'safari'


class UserAgentOperatingSystems:
    WINDOWS = 'windows'
    MACOS = 'macos'
    LINUX = 'linux'
    ANDROID = 'android'
    IOS = 'ios'


class UserAgentPlatforms:
    PC = 'pc'
    MOBILE = 'mobile'
    TABLET = 'tablet'


def generate_user_agent(
    browsers: UserAgentBrowsers | Iterable[UserAgentBrowsers] = None,
    operating_systems: UserAgentOperatingSystems | \
        Iterable[UserAgentOperatingSystems] = None,
    platforms: UserAgentPlatforms | Iterable[UserAgentPlatforms] = None
):
    kwargs = {}
    if browsers: kwargs['browsers'] = browsers
    if operating_systems: kwargs['os'] = operating_systems
    if platforms: kwargs['platforms'] = platforms
    return UserAgent(**kwargs).random
